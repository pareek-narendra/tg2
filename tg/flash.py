"""Flash messaging system for sending info to the user in a
non-obtrusive way
"""
from webflash import Flash
from pylons import response, request

from logging import getLogger

log = getLogger(__name__)

class TGFlash(Flash):
    def __call__(self, message, status=None, **extra_payload):
        # Force the message to be unicode so lazystrings, etc... are coerced
        return super(TGFlash, self).__call__(
            unicode(message), status, **extra_payload
            )

    @property
    def message(self):
        return self.pop_payload().get('message')

    @property
    def status(self):
        return self.pop_payload().get('status') or self.default_status
        
flash = TGFlash(
    get_response=lambda: response,
    get_request=lambda: request
    )

#TODO: Deprecate these?
def get_flash():
    """Returns the message previously set by calling flash()
    
    Additonally removes the old flash message """
    return flash.message

def get_status():
    """Returns the status of the last flash messagese
    
    Additonally removes the old flash message status"""
    return flash.status
