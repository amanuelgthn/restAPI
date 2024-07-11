import base64
import unittest

import app.client.crm


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.client.crm

    def test_class_exists_crmapiclient(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_class_function_exists_crmapiclient__check_response(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_crmapiclient__check_response(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cmVzcG9uc2U=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50Ll9jaGVja19yZXNwb25zZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`response`.",
        )

    def test_class_function_exists_crmapiclient_call(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_crmapiclient_call(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            10,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should have 10 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"bWV0aG9k").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`method`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"ZW5kcG9pbnQ=").decode(),
            args[2],
            msg=f"The argument #2 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`endpoint`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"ZGF0YQ==").decode(),
            args[3],
            msg=f"The argument #3 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`data`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"aw==").decode(),
            args[4],
            msg=f"The argument #4 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`k`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"dw==").decode(),
            args[5],
            msg=f"The argument #5 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`w`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YQ==").decode(),
            args[6],
            msg=f"The argument #6 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`a`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cg==").decode(),
            args[7],
            msg=f"The argument #7 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`r`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Zw==").decode(),
            args[8],
            msg=f"The argument #8 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`g`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q1JNQXBpQ2xpZW50").decode(),
            base64.b64decode(b"Q1JNQXBpQ2xpZW50LmNhbGw=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cw==").decode(),
            args[9],
            msg=f"The argument #9 of function "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50LmNhbGw=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q1JNQXBpQ2xpZW50').decode()}` "
            f"should be called "
            f"`s`.",
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
