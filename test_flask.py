import pytest, json, sys, os
import numpy as np
from app import app


class TestFlask:

    @staticmethod
    def request(data):
        """
        Makes a request to pix-cords endpoint with the given data.
        """
        url = 'http://0.0.0.0:5000/pix-cords'
        headers = {'Content-Type': 'text/plain','Accept': 'text/plain'}
        return app.test_client().post(url, data=data, headers=headers)


    @staticmethod
    def check_solution(data, img_dims, height, width):
        """
        Checks that the requirements hold for the solution.

        I'm choosing to return a string of the problem for better visibility when running pytest

        data: the decoded response from the post request
        img_dims: the image dimensions from the post request
        height, width: the height and width respectively of the rectangle
        returns: 'pass' if requirements hold, 'bad shape' if shape is wrong, 'bad space' if
                 the shape is wrong, 'bad order' if the ordering is wrong
        """
        data = np.array(eval(data)) # would do checks before doing eval() in production
        if (not TestFlask.good_shape(data, img_dims)):
            return 'bad shape'
        x = data[:,:,0].ravel()
        y = data[:,:,1].ravel()
        if (not TestFlask.good_space(x,y,img_dims,height,width)):
            return 'bad space'
        return 'pass'

    
    @staticmethod
    def good_shape(pts, img_dims):
        """
        Checks that the shape of the output is correct

        pts: np array of the points from the post request
        img_dims: tuple that's the image dimension parameter
        returns: true if shape is correct, else false
        """
        return pts.shape == (img_dims[1], img_dims[0], 2)

    
    @staticmethod
    def good_space(x,y,img_dims,height,width):
        """
        Checks that the pixels are evenly spaced

        Note: I interpret "evenly spaced" as having the distance between each pixel and its
        top/bottom and right/left neighbors as being the same. So it can be tested by just
        looking at the flattened x & y arrays.
        
        x: the x-coordinates of the pixels
        y: the y-coordinates of the pixels
        img_dims: parameters sent to the post request
        height, width: the height/width of the rectangle
        returns: true if "evenly spaced" pixels, false else
        """
        # there are img_dims[j] - 1 intervals to add, not img_dims[j] 
        expected_space = (width/(img_dims[0]-1), height/(img_dims[1]-1))
        epsilon = .0000001

        # loop L->R for x's, top->bottom for y's, only have to check each distance/edge once
        for idx in range(1, len(x)+1, 1):
            # python uses short circuiting so this shouldn't throw index errors
            if ((idx == 1 or idx-1 % img_dims[0] != 0) and idx < len(x) and x[idx] - x[idx-1] - expected_space[0] > epsilon):
                return False
            if (idx+img_dims[0] <= len(x) and y[idx-1] - y[idx-1 + img_dims[0]] - expected_space[1] > epsilon):
                return False
        return True

    
    def test_all_same(self):
        """
        Tests that the response is correct if all are the same.

        The spec says to return evenly spaced pixels within the rectangle defined by the corner
        points, so I think returning the same point in shape mxnx2 would be the only solution 
        here.
        """
        data = '(2,2),[(1,1),(1,1),(1,1),(1,1)]'
        resp = self.request(data)
        data = resp.data.decode('utf-8')

        assert data == '[[[1.0, 1.0], [1.0, 1.0]], [[1.0, 1.0], [1.0, 1.0]]]'
        
        
    def test_given_example(self):
        """
        Base test from the example provided in the spec.

        It also makes sure that white space is removed correctly.
        """

        data = '''(3,3),   [(1, 1), (3, 1), (1, 3), 


 (3, 3) ]'''
        resp = self.request(data)
        data = resp.data.decode('utf-8')

        assert resp.mimetype == 'text/plain'
        assert data == '[[[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]], [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]], [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]]'
        assert self.check_solution(data, (3,3), 2,2) == 'pass'
        

    def test_big_example(self):
        """
        Tests that the code works with a more points
        """
        pts =  [(1, 1), (3, 1), (1, 3), (3, 3)]
        data = '(100,300), ' + str(pts)
        resp = self.request(data)

        assert self.check_solution(resp.data.decode('utf-8'), (100,300), 2, 2) == 'pass'


    def test_negative_example(self):
        """
        Tests that the code works for negative numbers
        """
        pts = [(-1,-10),(-5,-10),(-1,-3),(-5,-3)]
        data = '(3,5),' + str(pts)
        resp = self.request(data)

        assert self.check_solution(resp.data.decode('utf-8'), (3,5), 7, 4) == 'pass'

        
    def another_test(self):
        """
        another test with randomly chosen inputs
        """
        pts =  [(-100, 20), (-100, -50), (30, 20), (30, -50) ]
        data =' (300,210),  ' + str(pts)
        resp = self.request(data)

        assert self.check_solution(resp.data.decode('utf-8'), (300,210), 70, 130)
        

    def test_content_type(self):
        """
        Tests that the right message and status are returned if the wrong content type is sent
        """
        data = '(3,3),   [(1, 1), (3, 1), (1, 3), (3, 3)]'
        url = 'http://0.0.0.0:5000/pix-cords'
        headers = {'Content-Type': 'applicatoin/json','Accept': 'text/plain'}
        resp = app.test_client().post(url, data=data, headers=headers)
        data = resp.data.decode('utf-8')
        
        assert data == '''Sorry, that content type is not supported.
    Usage: curl -X POST -H "Content-type: text/plain" -d "<image dimensions>,<corner points>" 0.0.0.0:5000/pix-cords'''
        assert resp.status == '400 BAD REQUEST'
        
