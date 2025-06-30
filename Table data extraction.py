## Table data extraction
# Yeh script webpage ke table se data extract karti hai using BeautifulSoup.

html='''
<table class="table table-bordered">
			<thead>
			<tr>
				<th>#</th>
				<th>First Name</th>
				<th>Last Name</th>
				<th>Username</th>
			</tr>
			</thead>
			<tbody>
			<tr>
				<td>1</td>
				<td>Mark</td>
				<td>Otto</td>
				<td>@mdo</td>
			</tr>
			<tr>
				<td>2</td>
				<td>Jacob</td>
				<td>Thornton</td>
				<td>@fat</td>
			</tr>
			<tr>
				<td>3</td>
				<td>Larry</td>
				<td>the Bird</td>
				<td>@twitter</td>
			</tr>
			</tbody>
		</table>

		<table class="table table-bordered table-bordered2">
			<thead>
			<tr>
				<th>#</th>
				<th>First Name</th>
				<th>Last Name</th>
				<th>Username</th>
			</tr>
			</thead>
			<tbody>
			<tr>
				<td>4</td>
				<td>Harry</td>
				<td>Potter</td>
				<td>@hp</td>
			</tr>
			<tr>
				<td>5</td>
				<td>John</td>
				<td>Snow</td>
				<td>@dunno</td>
			</tr>
			<tr>
				<td>6</td>
				<td>Tim</td>
				<td>Bean</td>
				<td>@timbean</td>
			</tr>
			</tbody>
		</table>
	</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Pehli table (class="table table-bordered") se data nikal rahe hain
tables = soup.find_all("table", class_="table table-bordered")
rows = tables[0].find_all("tr")

# Har row se first name, last name aur username print kar rahe hain
for row in rows[1:]:
    cols = row.find_all("td")
    first_name = cols[1].text
    last_name = cols[2].text
    username = cols[3].text
    print("First Name:", first_name, "Last Name:", last_name, ", Username:", username)

# Dusri table (class="table table-bordered table-bordered2") se data nikal rahe hain
tables = soup.find_all("table", class_="table table-bordered table-bordered2")
rows = tables[0].find_all("tr")

# Har row se first name, last name aur username print kar rahe hain
for row in rows[1:]:
    cols = row.find_all("td")
    first_name = cols[1].text
    last_name = cols[2].text
    username = cols[3].text
    print("First Name:", first_name, "Last Name:", last_name, ", Username:", username)