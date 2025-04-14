function generateRow(businessData, category) {
        let row = document.createElement("tr");
        let categoryCol = document.createElement("td");
        categoryCol.textContent = category;
        categoryCol.classList.add("category");
        row.appendChild(categoryCol)
        let sepCol = document.createElement("td");
        sepCol.textContent = " : ";
        row.appendChild(sepCol)

        let dataCol = document.createElement("td");
        dataCol.textContent = businessData[category];
        dataCol.classList.add("data");
        row.appendChild(dataCol)

        return row
}

function generator(){
        fetch("./workplaces.json").then(res => res.json()).then(data => {
                listingsTab = document.getElementById("listings")
                for (let businessCode in data){
                        businessData = data[businessCode]
                        let business = document.createElement("div")
                        business.classList.add("listing")
                        let imageColumn = document.createElement("div")
                        imageColumn.classList.add("imageColumn")
                        let image = document.createElement("a")
                        image.style.backgroundImage = "url(" + businessData["logo"] + ")"
                        image.classList.add("image")
                        image.href = businessData["Link"]
                        imageColumn.appendChild(image)


                        let textColumn = document.createElement("div")
                        textColumn.classList.add("textColumn")
                        let title = document.createElement("h1")
                        title.textContent = businessData["name"]
                        title.style.marginBottom = "0"
                        title.style.marginTop = "0"
                        textColumn.appendChild(title)

                        let table = document.createElement("table")
                        table.appendChild(generateRow(businessData, "Dates"));
                        table.appendChild(generateRow(businessData, "Hours"));
                        descriptionD = generateRow(businessData, "Description");
                        descriptionD.classList.add("desktop")
                        table.appendChild(descriptionD)
                        textColumn.appendChild(table)
                        descriptionM = document.createElement("p")
                        descriptionM.classList.add("mobile")
                        descriptionMTitle = document.createElement("h3")
                        descriptionMTitle.textContent = "Description: "
                        descriptionMTitle.classList.add("description", "mobile")
                        descriptionM.textContent = businessData["Description"]

                        textColumn.appendChild(descriptionMTitle)
                        textColumn.appendChild(document.createElement("br"))
                        textColumn.appendChild(descriptionM)




                        business.appendChild(imageColumn)
                        business.appendChild(textColumn)

                        listingsTab.appendChild(business)
                }
        })


}
window.addEventListener("scroll", function(){
        const scrollPercentage = (window.scrollY / (document.body.offsetHeight - window.innerHeight)) * 100;
        if (scrollPercentage >= 95) {
            generator();
        }})