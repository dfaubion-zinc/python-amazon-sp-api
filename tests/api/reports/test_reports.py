from __future__ import absolute_import
from sp_api.api import Reports
from sp_api.base import Marketplaces, Schedules, SellingApiBadRequestException, SellingApiServerException, \
    ProcessingStatus
from sp_api.base.reportTypes import ReportType


def test_create_report():
    res = Reports().create_report(
        reportType=ReportType.GET_MERCHANT_LISTINGS_ALL_DATA,
        dataStartTime=u'2019-12-10T20:11:24.000Z',
        marketplaceIds=[
            u"A1PA6795UKMFR9",
            u"ATVPDKIKX0DER"
        ])
    assert res.payload.get(u'reportId') == u'ID323'


def test_create_report_expect_400():
    try:
        res = Reports().create_report(
            reportType=u"BAD_FEE_DISCOUNTS_REPORT",
            dataStartTime=u"2019-12-10T20:11:24.000Z",
            marketplaceIds=[
                u"A1PA6795UKMFR9",
                u"ATVPDKIKX0DER"
            ])
    except SellingApiBadRequestException, br:
        assert br.code == 400


def test_create_report_expect_500():
    try:
        res = Reports().create_report(
            reportType=u"BAD_FEE_DISCasdafsdsfsdfsdOUNTS_REPORT",
            dataStartTime=u"2019-12-10T20:11:24.000Z",
            marketplaceIds=[
                u"A1PA6asfd795UKMFR9",
                u"ATVPDKIKX0DER"
            ])
    except SellingApiServerException, br:
        assert br.code == 500


def test_get_report():
    res = Reports().get_report(u'ID323')
    assert res.payload.get(u'reportId') == u'ReportId1'
    assert res.payload.get(u'reportType') == u'FEE_DISCOUNTS_REPORT'


def test_get_report_document_n_decrypt():
    res = Reports().get_report_document(u'0356cf79-b8b0-4226-b4b9-0ee058ea5760', decrypt=False)
    assert res.errors is None
    assert u'document' not in res.payload


def test_create_report_schedule():
    res = Reports().create_report_schedule(reportType=u'FEE_DISCOUNTS_REPORT',
                                           period=Schedules.MINUTES_5.value,
                                           nextReportCreationTime=u"2019-12-10T20:11:24.000Z",
                                           marketplaceIds=[u"A1PA6795UKMFR9", u"ATVPDKIKX0DER"])
    assert res.errors is None
    assert u'reportScheduleId' in res.payload


def test_delete_schedule_by_id():
    res = Reports().delete_report_schedule(u'ID')
    assert res.errors is None


def test_get_schedule_by_id():
    res = Reports().get_report_schedule(u'ID323')
    assert res.errors is None
    assert u'period' in res.payload
    assert res.payload.get(u'reportType') == u'FEE_DISCOUNTS_REPORT'


def test_get_reports_1():
    report_types = [
        u"FEE_DISCOUNTS_REPORT",
        u"GET_AFN_INVENTORY_DATA"
    ]
    processing_status = [
        u"IN_QUEUE",
        u"IN_PROGRESS"
    ]
    res = Reports().get_reports(reportTypes=report_types, processingStatuses=processing_status)
    assert res.errors is None


def test_get_reports_2():
    report_types = [
        u"FEE_DISCOUNTS_REPORT",
        u"GET_AFN_INVENTORY_DATA"
    ]
    processing_status = [
        ProcessingStatus.IN_QUEUE,
        ProcessingStatus.IN_PROGRESS
    ]
    res = Reports().get_reports(reportTypes=report_types, processingStatuses=processing_status)
    assert res.errors is None


def test_get_reports_3():
    report_types = [
        ReportType.FEE_DISCOUNTS_REPORT,
        ReportType.GET_AFN_INVENTORY_DATA
    ]
    processing_status = [
        ProcessingStatus.IN_QUEUE,
        ProcessingStatus.IN_PROGRESS
    ]
    res = Reports().get_reports(reportTypes=report_types, processingStatuses=processing_status)
    assert res.errors is None


def test_get_reports_4():
    report_types = [
        ReportType.FEE_DISCOUNTS_REPORT,
        ReportType.GET_AFN_INVENTORY_DATA
    ]
    processing_status = [
        ProcessingStatus.IN_QUEUE,
        ProcessingStatus.IN_PROGRESS
    ]
    res = Reports().get_reports(reportTypes=report_types, processingStatuses=processing_status,
                                marketplaceIds=[Marketplaces.US, Marketplaces.US.marketplace_id])
    assert res.errors is None
