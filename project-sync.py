import openshift as oc

with oc.tracking() as tracker:
    try:
        print('Current user: {}'.format(oc.whoami()))
    except:
        print('Error acquiring current username')
    
    # Print out details about the invocations made within this context.
    print(tracker.get_result())