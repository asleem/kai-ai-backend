import pytest
from app.features.ai_resistant_assignment_generator.core import executor
from app.services.schemas import AIResistantArgs

def test_executor_pdf_url_valid():

    ai_resistant_args = AIResistantArgs(
        topic = "Introduction to Data Science",
        assignment = "Develop a Neural Network Architecture for emulating Data Science Workflow",
        grade_level = "college",
        file_type = "pdf",
        file_url = "http://ijsmsjournal.org/2021/volume-4%20issue-4/ijsms-v4i4p137.pdf",
        lang = "en"
    )
    assignment = executor(ai_resistant_args)

    assert isinstance(assignment, list)
    assert len(assignment) == 3


def test_executor_pdf_url_invalid():

    ai_resistant_args = AIResistantArgs(
        topic = "Introduction to Data Science",
        assignment = "Develop a Neural Network Architecture for emulating Data Science Workflow",
        grade_level = "college",
        file_type = "pdf",
        file_url = "http://ijsmsjournal.org/2021/volume-4%20issue-4/dummy.pdf",
        lang = "en"
    )

    with pytest.raises(ValueError) as exc_info:
        assignment = executor(ai_resistant_args)

    assert isinstance(exc_info.value, ValueError)