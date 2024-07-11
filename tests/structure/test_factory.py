import base64
import unittest

import app.factory


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.factory

    def test_function_exists_api_crm_client_factory(self):
        functions = _get_function_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"YXBpX2NybV9jbGllbnRfZmFjdG9yeQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'YXBpX2NybV9jbGllbnRfZmFjdG9yeQ==').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_function_signature_match_api_crm_client_factory(self):
        functions = _get_function_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"YXBpX2NybV9jbGllbnRfZmFjdG9yeQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'YXBpX2NybV9jbGllbnRfZmFjdG9yeQ==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        args = _get_function_arg_names(
            self.MODULE, base64.b64decode(b"YXBpX2NybV9jbGllbnRfZmFjdG9yeQ==").decode()
        )
        self.assertEqual(
            0,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'YXBpX2NybV9jbGllbnRfZmFjdG9yeQ==').decode()}` "
            f"should have exactly 0 argument(s).",
        )


# === Internal functions, do not modify ===
import inspect

from types import ModuleType
from typing import List


def _get_function_names(module: ModuleType) -> List[str]:
    names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            names.append(name)
    return names


def _get_function_arg_names(module: ModuleType, fn_name: str) -> List[str]:
    arg_names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            if fn.__qualname__ == fn_name:
                args_spec = inspect.getfullargspec(fn)
                arg_names = args_spec.args
                if args_spec.varargs is not None:
                    arg_names.extend(args_spec.varargs)
                if args_spec.varkw is not None:
                    arg_names.extend(args_spec.varkw)
                arg_names.extend(args_spec.kwonlyargs)
                break
    return arg_names


def _get_class_names(module: ModuleType) -> List[str]:
    names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for name, cls in classes:
        if cls.__module__ == module.__name__:
            names.append(name)
    return names


def _get_class_function_names(module: ModuleType, cls_name: str) -> List[str]:
    fn_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name, fn in functions:
                    fn_names.append(fn.__qualname__)
                break
    return fn_names


def _get_class_function_arg_names(
    module: ModuleType, cls_name: str, fn_name: str
) -> List[str]:
    arg_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name_, fn in functions:
                    if fn.__qualname__ == fn_name:
                        args_spec = inspect.getfullargspec(fn)
                        arg_names = args_spec.args
                        if args_spec.varargs is not None:
                            arg_names.extend(args_spec.varargs)
                        if args_spec.varkw is not None:
                            arg_names.extend(args_spec.varkw)
                        arg_names.extend(args_spec.kwonlyargs)
                        break
                break
    return arg_names
