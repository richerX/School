import dataclasses
import inspect
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


@attr.s(frozen=True, order=True, slots=True)
class AttrComment:
    id: int = 0
    text: str = ""


def main():
    comment = Comment(1, "I just subscribed!")
    # comment.id = 3  # can't immutable
    print(comment)
    print(dataclasses.astuple(comment))
    print(dataclasses.asdict(comment))
    copy = dataclasses.replace(comment, id=3)
    print(copy)

    print(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == '__main__':
    main()