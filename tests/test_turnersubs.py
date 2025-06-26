import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from turnersubs.main import get_images


def test_get_images(tmp_path):
    (tmp_path / "img_01.png").write_bytes(b'\x89PNG\r\n\x1a\n')
    (tmp_path / "img_02.jpg").write_bytes(b'JFIF')
    images = get_images(tmp_path)
    assert images == [os.path.join(tmp_path, 'img_01.png'), os.path.join(tmp_path, 'img_02.jpg')]

