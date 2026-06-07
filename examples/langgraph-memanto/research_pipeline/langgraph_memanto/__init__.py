</solution> </solution> <solution>def mattpocock_solution() -> None:  # Public API
    # Initialize Mattpocock flow
    # ...
    # Inject retrievals into run context
    # ...
    # Store post-run extraction/state

ACTUAL REPO CODE (use these exact function names, imports, and patterns):
// FILE: examples/langgraph-memanto/memanto_tools.py
from __future__ import annotations

from typing import Annotated, Literal

from langchain_core.tools import tool
from pydantic import Field

from memanto.cli.client.sdk_client import SdkClient

VALID_MEMORY_TYPES = (
    "fact (objective truths/data), "
    "preference (user likes/dislikes), "
    "goal (objectives/targets), "
    "decision (choices made/agreed upon), "
    "artifact (files/code/deliverables), "
    "learning (insights/lessons learned), "
    "event (occurrences/meetings), "
    "instruction (how-tos/directives), "
    "relationship (connections between entities), "
    "context (background info/state), "
    "observation (trends/patterns/notices), "
    "commitment (promises/next steps), "
    "error (failures/mistakes)"
)

MemoryType = Literal[
    "fact",
    "preference",
    "goal",
    "decision",