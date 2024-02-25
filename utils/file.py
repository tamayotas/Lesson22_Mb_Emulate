def abs_path_from_project(relative_path: str):
    import Lesson22_Mb_Emulate
    from pathlib import Path

    return (
        Path(Lesson22_Mb_Emulate.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )