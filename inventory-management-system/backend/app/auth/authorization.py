from functools import wraps


def admin_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):

        if user.role != "admin":
            raise PermissionError(
                "Admin access required"
            )

        return func(user, *args, **kwargs)

    return wrapper



def common_user_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):

        if user.role != "common":
            raise PermissionError(
                "Common user access required"
            )

        return func(user, *args, **kwargs)

    return wrapper



def check_branch_access(user, branch_id):

    if user.role == "admin":
        return False

    return user.branch_id == branch_id