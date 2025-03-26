import React from 'react';

const columns = [
    {header: 'file', accessor: 'fileName'},
    { header: 'Reason', accessor: 'Reason' },
    { header: 'Confidence Score', accessor: 'confidenceScore' },
    { header: 'duplicateIndicator', accessor: 'duplicateIndicator' },
    { header: 'Date', accessor: 'Date' },
    { header: 'To', accessor: 'To' },
    { header: 'Request Type', accessor: 'requestType' },
    { header: 'Sub Request Type', accessor: 'subRequestType' },
];

function Table({dataResponse}) {
  const data = Object.keys(dataResponse).map((key) => {
    console.log(dataResponse[key]);
    return {
      'fileName': key,
      'Reason': dataResponse[key]['Reason'] || 'N/A',
      'confidenceScore': dataResponse[key]['confidenceScore'] || 'N/A',
      'duplicateIndicator': dataResponse[key]['duplicateIndicator'] || 'N/A',
      'Date': dataResponse[key]['extracted_fields'].Date,
      'To': dataResponse[key]['extracted_fields'].To,
      'requestType': dataResponse[key]['requestType'],
      'subRequestType': dataResponse[key]['subRequestType'],
    }
  });

  return (
    <div>
      <table border="1" style={{ width: '100%', textAlign: 'left', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            {columns.map((column, index) => (
              <th key={index}>{column.header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data && data.length > 0 ? (
            data.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {columns.map((column, colIndex) => (
                  <td key={colIndex}>{row[column.accessor]}</td>
                ))}
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={columns.length} style={{ textAlign: 'center' }}>
                No data available.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Table;