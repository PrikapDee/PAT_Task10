from guvi_insta import Guvi
import pytest

url = "https://www.instagram.com/guviofficial/"

guvi_obj1 = Guvi(url)


# test to verify followers count
def test_count_followers():
    # expected variable value to compare it with method actual value
    count_followers = '165K'
    assert guvi_obj1.get_count_followers() == count_followers
    print("Testcase pass")


# test to verify following count
def test_count_following():
    # expected variable value to compare it with method actual value
    count_following = '6'
    assert guvi_obj1.get_count_following() == count_following
    print("testcase pass")
