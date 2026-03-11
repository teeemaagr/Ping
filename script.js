function loadStatus() {
    fetch("/api/status")
        .then(res => res.json())
        .then(data => {
            const tableBody = document.getElementById("table-body");
            tableBody.innerHTML = "";

            data.forEach(item => {
                const row = document.createElement("tr");
               const statusClass = item.status ? "status-online" : "status-offline";

               row.innerHTML = `
                <td>${item.ip}</td>
                <td class="${statusClass}">
    ${item.status ? "🟢 Online" : "🔴 Offline"}
</td>
`;

                tableBody.appendChild(row);
            });
        });
}

loadStatus();
setInterval(loadStatus, 5000);