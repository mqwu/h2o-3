from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import threading
from h2o.utils.typechecks import assert_is_type

def h2ocluster_shutdown():
    """
    Python API test: h2o.cluster().shutdown(prompt=False)
    """
    try:
        bthread = threading.Thread(target=call_badshutdown())
        bthread.daemon=True
        bthread.start()
        bthread.join(1.0)
    except Exception as e:
        print("*** Error in thread is caught=> ")
        print(e)    # if we see this warning message, the error is caught correctly
        assert_is_type(e, TypeError)
        assert "badparam" in e.args[0], "h2o.shutdown() command is not working."


    thread = threading.Thread(target=call_shutdown)
    thread.daemon =True
    thread.start()
    thread.join(1.0)

def call_shutdown():
    h2o.cluster().shutdown(prompt=True)   # call shutdown but do not actually shut anything down.

def call_badshutdown():
    h2o.cluster().shutdown(badparam=1, prompt=True)   # call shutdown but do not actually shut anything down.

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ocluster_shutdown)
else:
    h2ocluster_shutdown()
