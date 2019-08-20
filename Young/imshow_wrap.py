BackendError = type('BackendError', (Exception,), {})


def _is_visible(winname):
    try:
        ret = cv2.getWindowProperty(
            winname, cv2.WND_PROP_VISIBLE
        )

        if ret == -1:
            raise BackendError('Use Qt as backend to check whether window is visible or not.')

        return bool(ret)

    except cv2.error:
        return False


ORD_ESCAPE = 0x1b


def closeable_imshow(winname, img, *, break_key=ORD_ESCAPE):
    while True:
        cv2.imshow(winname, img)
        key = cv2.waitKey(10)

        if key == break_key:
            break
        if not _is_visible(winname):
            break

    cv2.destroyWindow(winname)

