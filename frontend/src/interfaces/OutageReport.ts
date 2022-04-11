export interface OutageReport{
    report_id: string,
    client_id: string,
    company_id: string,
    title: string,
    date: string,
    time: string,
    description?: string,
    status: string,
    cause?: string,
}