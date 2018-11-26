## Software environment  
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [GitDash](https://git-scm.com/downloads)

## How to Install
1. Install Vagrant & VirtualBox & Gitdash
2. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`) in GitDash
4. Log into Vagrant VM (`vagrant ssh`) in GitDash
5. Navigate to `cd/vagrant` as instructed in terminal
6. Then type cd item-Catalog-Application-master/Item-Catalog
7. database has already setup and imported the fake data,
8. Run application using `python project.py`
9. Access the application locally using http://localhost:8000



## JSON Endpoints
The following are open to the public:

Catalog JSON: `/catalog/JSON`
    - Displays the whole catalog. Categories and all items.

Categories JSON: `/catalog/categories/JSON`
    - Displays all categories

Category Items JSON: `/catalog/<path:category_name>/items/JSON`
    - Displays items for a specific category

Category Item JSON: `/catalog/<path:category_name>/<path:item_name>/JSON`
    - Displays a specific category item.
