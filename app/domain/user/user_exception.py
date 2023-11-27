class UserNotFoundError(Exception):
    message = "The user hasn't been found."

    def __str__(self):
        return UserNotFoundError.message


class UserAlreadyExistsError(Exception):
    message = "The user already exists."

    def __str__(self):
        return UserAlreadyExistsError.message

class UserNotCreatedError(Exception):
    message = "The user can't be created."

    def __str__(self):
        return UserNotCreatedError.message

class UsersNotFoundError(Exception):
    message = "No Users have been found."

    def __str__(self):
        return UserNotFoundError.message