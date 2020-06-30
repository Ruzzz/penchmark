from ._defs import ByDataReport, Callee, InData, Report, ReportItem, Summary, SummaryItem
from ._report import report_as_md_table
from ._core import benchmark, NameGenerator


def benchmark_and_print(*args, **kwargs):
    print(report_as_md_table(*benchmark(*args, **kwargs)))
