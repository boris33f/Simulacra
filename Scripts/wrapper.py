def _inject_to_cls_method(cls, method_name, before: False):
    def decorator(hook_fn):
        original_method = getattr(cls, method_name)

        def wrapper(*args, **kwargs):
            if before:
                hook_fn(*args, **kwargs)
                result = original_method(*args, **kwargs)
            else:
                result = original_method(*args, **kwargs)
                hook_fn(*args, **kwargs)

            return result

        setattr(cls, method_name, wrapper)
        return wrapper

    return decorator


def inject_before_cls_method(cls, method_name):
    return _inject_to_cls_method(cls, method_name, before=True)

def inject_after_cls_method(cls, method_name):
    return _inject_to_cls_method(cls, method_name, before=False)


def run_after_fn(target_fn):
    def decorator(current_fn):
        def wrapper(*args, **kwargs):
            result = target_fn(*args, **kwargs)
            current_fn(*args, **kwargs)
            return result

        globals()[target_fn.__name__] = wrapper

        return current_fn
    return decorator