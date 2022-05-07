import React from 'react';
import { useTable } from 'react-table';
import ReactTable from 'react-table';


function OutageReportTable() {
    const data = React.useMemo(() =>
        [{
            service: 'Electricity',
            title: 'Outage in San Juan',
            date: '05/7',
            time: '01:36',
          
            status: 'Unsolved',
        },
        {
            service: 'Water',
            title: '4420 Valley Street, Garnerville, NY 10923',
            date: '07/11',
            time: "21:31",
           
            status: 'Resolved',
        },
        {
            service: 'Electricity',
            title: '4420 Valley Street, Garnerville, NY 10923',
            date: '07/11',
            time: '22:22',
          
            status: 'Unsolved',
        },
        {
            service: 'Internet',
            title: '4420 Valley Street, Garnerville, NY 10923',
            date: '07/11',
            time: '22:22',
        
            status: 'Outdated',
        },
        {
            service: 'Water',
            title: '4420 Valley Street, Garnerville, NY 10923',
            date: '07/11',
            time: '22:22',
         
            status: 'Unsolved',
        },
        {
            service: 'Water',
            title: '4420 Valley Street, Garnerville, NY 10923',
            date: '07/11',
            time: '22:22',
         
            status: 'Unsolved',
        },
        ],
        []
        );

    const columns = React.useMemo(
            () => [
            {
                Header: 'Outage Reports',
                columns: [
                {
                Header: 'Service Affected',
                accessor: 'service',
                },
                {
                Header: 'Title',
                accessor: 'title',
                },
                {
                Header: 'Date',
                accessor: 'date',
                },
                {
                Header: 'Time',
                accessor: 'time',
                },
                {
                Header: 'Status',
                accessor: 'status',
                style: 'background:white;cursor:pointer',
                }
                ]
            }
            ],
            []
           )
       
    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        rows,
        prepareRow,
        } = useTable({ columns, data })
    
    const rowStyle = {
        color:"black",
        background:"white",
        padding:5,
        cursor:"pointer"
    }

  return (
    <div>
        <table {...getTableProps()} className="table" style={{color:'black',background:'black'}}>
        <thead>
            {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()} >
                {headerGroup.headers.map(column => (
                <th {...column.getHeaderProps()} style={rowStyle}>{column.render('Header')}</th>
                ))}
            </tr>
            ))}
        </thead>
        <tbody {...getTableBodyProps()}>
            {rows.map(row => {
            prepareRow(row)
            return (
                <tr {...row.getRowProps()}>
                {row.cells.map(cell => {
                    return <td style={rowStyle} {...cell.getCellProps() }>{cell.render('Cell')}</td>
                })}
                </tr>
            )
            })}
        </tbody>
    </table>
    </div>
  )
}

export default OutageReportTable