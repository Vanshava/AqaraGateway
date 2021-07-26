"""Constants of the Xiaomi Aqara Lock."""

WITH_LI_BATTERY = 1
SUPPORT_ALARM = 2
SUPPORT_DOORBELL = 4
SUPPORT_CAMERA = 8
SUPPORT_WIFI = 16

DEVICE_MAPPINGS = {
    "lumi.lock.aq1": SUPPORT_ALARM,
    "lumi.lock.acn02": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "lumi.lock.acn03": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "aqara.lock.wbzac1": (
        WITH_LI_BATTERY | SUPPORT_ALARM |
        SUPPORT_DOORBELL | SUPPORT_WIFI | SUPPORT_CAMERA),
    "aqara.lock.bzacn4": (
        SUPPORT_ALARM | SUPPORT_DOORBELL)
}

LOCK_NOTIFICATIOIN = {
    "latch_state": {
        "default": "Latch state changed",
        "0": "Remove the locking from inside",
        "1": "Reverse locked"},
    "lock": {
        "default": "Lock state changed",
        "0": "Door is open",
        "1": "Door is closed",
        "2": "Door is not close",
        "3": "Doorbell is ringing",
        "4": "Lock is damaged"},
    "door": {
        "default": "door state changed",
        "0": "Door is open",
        "1": "Open Door",
        "2": "Door is not close"},
    "unlock from inside": {"default": "Unlock from Inside"},
    "someone detected": {"default": "Someone is lingering at the door"},
    "li battery notify":
        {"default": "Li Battery notify",
         "0": "Li Battery is abnormal",
         "1": "Li Battery is normal"},
    "battery notify":
        {"default": "Battery notify",
         "0": "Battery is abnormal",
         "3": "Battery is normal"},
    "camera connected": {"default": "Camera is connected"},
    "open in away mode": {
        "default":
            "In the Away-from-home Mode, someone opens the door indoors"},
    "lock by handle": {"default": "Lock by door handle"},
    "unlock by password": {"default": "Unlocked with Keypad by user"},
    "unlock by fringprint": {"default": "Unlocked with Fringprint by user"},
    "unlock by bluetooth": {"default": "Unlocked with Bluetooht by user"},
    "unlock by homekit": {"default": "Unlocked with HomeKit by user"},
    "unlock by key": {"default": "Unlocked with key by user"},
    "away mode": {
        "default": "Away mode changed",
        "0": "Away-from-home mode is removed",
        "1": "Away-from-home mode is enabled"},
    "nfc added": {"default": "Added NFC card or Tag"},
    "verification failed": {"default": "door lock verifications failed"},
    "user_1": {
        "default": "Unlocked with Keypad by user 1",
        "1": "User Added",
        "2": "User Removed"},
    "user_2": {
        "default": "Unlocked with Keypad by user 2",
        "1": "User Added",
        "2": "User Removed"},
}
