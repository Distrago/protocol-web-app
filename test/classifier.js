//Таблицы
var productNameList = [];
var productTypeList = [];
var weedNameList = [];
var weedClassList = []
var descriptionList = [];

var componentPartsList = [];
var componentStatusList = [];
var componentColorList = [];

var clsDropdown;
//Протокол
var protocol = [];
var fiel;
var allNames = document.getElementsByName('fractionSource');

var componentElementClassifier = {
	classifierType: 0,
	classifierProduct: {
		useADD: false,
		mainOptions:{
			industryID: 9999,
			groupProductID: 9999,
			productID: 9999,
			descriptionID: 9999,
			productTypeID: 9999,
			productSortID: 9999,
			purposeID: 9999,
			GOST_ID: 9999,
			partsID: 9999,
			statusID: 9999
		},
		addCustomOption: ""
	},
	classifierWeed:{
		useADD: false,
		mainOptions:{
			industryID: 9999,
			categoryID: 9999,
			classWeedID: 9999,
			weedNameID: 9999,
			descriptionID: 9999,
			colorID: 9999
		},
		addCustomOption: "" 
	}
};

function startApp(){//check
	read_industry();
	get_protocolTop();
	img_script();
	ewe();	
	addrow();
	addrow();
	//Временные переключатели
	document.getElementsByClassName("toggle")[0].addEventListener("click", switchToggle);
	document.getElementsByClassName("toggle")[1].addEventListener("click", switchToggle);
	document.getElementsByClassName("toggle")[2].addEventListener("click", switchToggle);
	
	setupRequirementsTable();
}

function StartInput(idRow){//check
	var inputBlock = document.getElementById("clsInput_test_" + idRow);
	var clsDropdown = document.getElementById("clsDropdown_" + idRow);
	DoropdownOptionClear(idRow);
	if(inputBlock.value.length == 0){
		DropdownOptionDefault(idRow)
	}
	else{
		DropdownSearch(idRow)
	}	
	clsDropdown.style.display="flex";
}
function StartInputListeners(idRow){//check
	return function e(){
		var inputBlock = document.getElementById("clsInput_test_" + idRow);
		var clsDropdown = document.getElementById("clsDropdown_" + idRow);
		DoropdownOptionClear(idRow);
		if(inputBlock.value.length == 0){
			DropdownOptionDefault(idRow)
		}
		else{
			DropdownSearch(idRow)
		}	
		clsDropdown.style.display="flex";
	}
}
function DoropdownOptionClear(idRow){//check
	var clsDropdown = document.getElementById("clsDropdown_" + idRow);
	var dropdownOptions = clsDropdown.children[0];
	//Стартовая отчиска от лишних элементов
	for(var i = dropdownOptions.children.length - 1; i > 0; i--){
		dropdownOptions.children[i].remove();
	}
}
function setupTableInfo(){//check
	//Продукты
	for(var i = 0; i < list_product.length; i++){
		productNameList.push({
			"id": list_product[i].id_product,
			"name": list_product[i].productName
		});
	}
	//Засорители
	for(var i = 0; i < list_weed.length; i++){
		weedNameList.push({
			"id": list_weed[i].id_weed,
			"name": list_weed[i].weedName
		});
	}
	//Тип продукта(описание);
	for(var i = 0; i < list_productType.length; i++){
		if(list_productType[i].productTypeName != "-"){
			productTypeList.push({
				"id": list_productType[i].id_productType,
				"name": list_productType[i].productTypeName
			});
		}
	}
	//Классы засорителя
	for(var i = 0; i < list_classWeed.length; i++){
		weedClassList.push({
			"id": list_classWeed[i].id_class,
			"name": list_classWeed[i].className
		});
	}
	//Описания семян(зерна)
	for(var i = 0; i < list_descriptionSeed.length; i++){
		descriptionList.push({
			"id": list_descriptionSeed[i].id_description,
			"name": list_descriptionSeed[i].descriptionName
		});
	}
	//Дополнительные описания для компонетов(продуктов и засорителей)
	for(var i = 0; i < list_productPart.length; i++){
		componentPartsList.push({
			"id": list_productPart[i].id_number,
			"name": list_productPart[i].productPart
		})
	}
	for(var i = 0; i < list_productStatus.length; i++){
		componentStatusList.push({
			"id": list_productStatus[i].id_number,
			"name": list_productStatus[i].productStatus
		})
	}
	for(var i = 0; i < list_productColor.length; i++){
		componentColorList.push({
			"id": list_productColor[i].id_number,
			"name": list_productColor[i].productColor
		})
	}
}
function returnTableType(tableID){//check
	switch(tableID){
		case productNameList:
			var id = "product";
			break;
		case productTypeList:
			var id = "productType";
			break;
		case weedNameList:
			var id =  "weed";
			break;
		case weedClassList:
			var id =  "weedClass";
			break;
		case descriptionList:
			var id = "discription";
			break;
		case componentPartsList:
			var id = "parts";
			break;
		case componentStatusList:
			var id = "status";
			break;
		case componentColorList:
			var id = "color";
			break;
	}
	return id;
}
function DropdownOptionDefault(idRow){//check
	var clsDropdown = document.getElementById("clsDropdown_" + idRow);
	var dropdownOptions =  clsDropdown.children[0];
	var dropdownOptionClone = clsDropdown.children[0].children[0];
	var classifierInpurResult = document.getElementById("classifierInpurResult_" + idRow);
	
	var listElements = [productNameList, weedNameList, productTypeList, weedClassList, descriptionList, componentPartsList, componentStatusList, componentColorList];
	
	//Проверки
	for(var i = 0; i < classifierInpurResult.children.length; i++){
		var resultType = classifierInpurResult.children[i].id.split('_')[1];
		if(resultType == "product"){
			var ID_product = Number(classifierInpurResult.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, productNameList);
			listElements = checkResultOption(listElements, weedNameList);
			listElements = checkResultOption(listElements, componentColorList);
		}
		if(resultType == "weed"){
			var ID_weed = Number(classifierInpurResult.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, productNameList);
			listElements = checkResultOption(listElements, weedNameList);
			listElements = checkResultOption(listElements, descriptionList);
			listElements = checkResultOption(listElements, componentPartsList);
			listElements = checkResultOption(listElements, componentStatusList);
		}
		if(resultType == "productType"){
			var ID_productType = Number(classifierInpurResult.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, weedNameList);
			listElements = checkResultOption(listElements, productTypeList);
		}
		if(resultType == "weedClass"){
			var ID_weedClass = Number(classifierInpurResult.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, productNameList);
			listElements = checkResultOption(listElements, weedClassList);
			listElements = checkResultOption(listElements, descriptionList)
		}
		if(resultType == "discription"){
			listElements = checkResultOption(listElements, descriptionList);
			listElements = checkResultOption(listElements, weedNameList);
		}
		if(resultType == "parts"){
			listElements = checkResultOption(listElements, componentPartsList);
		}
		if(resultType == "status"){
			listElements = checkResultOption(listElements, componentStatusList);
		}
		if(resultType == "color"){
			listElements = checkResultOption(listElements, componentColorList);
		}
	}
	
	for(var i = 0; i < listElements.length; i++){
		var __list = listElements[i];	
		if(__list == productNameList || __list == weedNameList){
			if(ID_productType == null && ID_weedClass == null){
				for(var k = 0; k < list_protocolTop.length; k++){
					for(var el = 0 ; el < __list.length; el++){
						if(list_protocolTop[k] == __list[el].name){
							var option = dropdownOptionClone.cloneNode(true);
							option.style.display = "";
							option.children[0].setAttribute('name', returnTableType(listElements[i]));
							option.children[0].id = returnTableType(listElements[i]) + "_" + __list[el].id;
							option.children[0].value = __list[el].name;
							dropdownOptions.appendChild(option);
							
							option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
							break;
						}
					}
				}
			}
			else if(ID_productType != null){
				var id = list_productType[ID_productType].id_product;
				var option = dropdownOptionClone.cloneNode(true);
				option.style.display = "";
				option.children[0].setAttribute('name', "product");
				option.children[0].id =  "product_" + list_product[id].id_product;
				option.children[0].value = list_product[id].productName;
				dropdownOptions.appendChild(option);
				
				option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
			}
			else if (ID_weedClass != null){
				for(var k = 0; k < list_weed.length; k++){
					if(list_weed[k].id_class == ID_weedClass){
						var option = dropdownOptionClone.cloneNode(true);
						option.style.display = "";
						option.children[0].setAttribute('name', "weed");
						option.children[0].id = "weed_" + list_weed[k].id_weed;
						option.children[0].value = list_weed[k].weedName;
						dropdownOptions.appendChild(option);
						
						option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
					}
				}
			}
		}
		else if(__list == productTypeList && ID_product != null){
			for(var k = 0; k < list_productType.length; k++){
				for(var el = 0 ; el < __list.length; el++){
					if(list_productType[k].id_product == ID_product && list_productType[k].productTypeName == __list[el].name){
						var option = dropdownOptionClone.cloneNode(true);
						option.style.display = "";
						option.children[0].setAttribute('name', returnTableType(listElements[i]));
						option.children[0].id = returnTableType(listElements[i]) + "_" + __list[el].id;
						option.children[0].value = __list[el].name;
						dropdownOptions.appendChild(option);
						
						option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
						break;
					}
				}
			}
		}
		else if(__list == weedClassList && ID_weed != null){
			for(var k = 0; k < list_classWeed.length; k++){
				for(var el = 0 ; el < __list.length; el++){
					if(list_classWeed[k].id_class == list_weed[ID_weed].id_class && list_classWeed[k].className == __list[el].name){
						var option = dropdownOptionClone.cloneNode(true);
						option.style.display = "";
						option.children[0].setAttribute('name', returnTableType(listElements[i]));
						option.children[0].id = returnTableType(listElements[i]) + "_" + __list[el].id;
						option.children[0].value = __list[el].name;
						dropdownOptions.appendChild(option);
						
						option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
						break;
					}
				}
			}
		}
		else if (__list == descriptionList && (ID_product != null || ID_weed != null)){
			for(var el = 0 ; el < __list.length; el++){
				var option = dropdownOptionClone.cloneNode(true);
				option.style.display = "";
				option.children[0].setAttribute('name', returnTableType(listElements[i]));
				option.children[0].id = returnTableType(listElements[i]) + "_" + __list[el].id;
				option.children[0].value = __list[el].name;
				dropdownOptions.appendChild(option);
				
				option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
			}
			break;
		}
		else if((__list == componentPartsList || __list == componentStatusList || __list == componentColorList) && (ID_product != null || ID_weed != null)){
			for(var el = 0 ; el < __list.length; el++){
				var option = dropdownOptionClone.cloneNode(true);
				option.style.display = "";
				option.children[0].setAttribute('name', returnTableType(listElements[i]));
				option.children[0].id = returnTableType(listElements[i]) + "_" + __list[el].id;
				option.children[0].value = __list[el].name;
				dropdownOptions.appendChild(option);
				
				option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
			}
			break;
		}
	}

}
function DropdownSearch(idRow){//check
	var inputBlock = document.getElementById('clsInput_test_' + idRow);
	var dropdownBlock = document.getElementById('clsDropdown_' + idRow);
	var classifierInpurResultRow = document.getElementById('classifierInpurResult_' + idRow);
	var dropdownOptions = dropdownBlock.children[0];
	var dropdownOptionClone = dropdownBlock.children[0].children[0];
	
	var listElements = [productNameList, weedNameList, productTypeList, weedClassList, descriptionList, componentPartsList, componentStatusList, componentColorList];
	//Проверки
	for(var i = 0; i < classifierInpurResultRow.children.length; i++){
		var resultType = classifierInpurResultRow.children[i].id.split('_')[1];
		if(resultType == "product"){
			var ID_product = Number(classifierInpurResultRow.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, productNameList);
			listElements = checkResultOption(listElements, weedNameList);
			listElements = checkResultOption(listElements, componentColorList);
		}
		if(resultType == "weed"){
			var ID_weed = Number(classifierInpurResultRow.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, productNameList);
			listElements = checkResultOption(listElements, weedNameList);
			listElements = checkResultOption(listElements, descriptionList);
			listElements = checkResultOption(listElements, componentPartsList);
			listElements = checkResultOption(listElements, componentStatusList);
		}
		if(resultType == "productType"){
			var ID_productType = Number(classifierInpurResultRow.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, weedNameList);
			listElements = checkResultOption(listElements, productTypeList);
		}
		if(resultType == "weedClass"){
			var ID_weedClass = Number(classifierInpurResultRow.children[i].id.split('_')[2]);
			listElements = checkResultOption(listElements, productNameList);
			listElements = checkResultOption(listElements, weedClassList);
		}
		if(resultType == "discription"){
			listElements = checkResultOption(listElements, descriptionList);
			listElements = checkResultOption(listElements, weedNameList);
		}
		if(resultType == "parts"){
			listElements = checkResultOption(listElements, componentPartsList);
		}
		if(resultType == "status"){
			listElements = checkResultOption(listElements, componentStatusList);
		}
		if(resultType == "color"){
			listElements = checkResultOption(listElements, componentColorList);
		}
	}	
	//Поиск/определение
	for(var id = 0; id < listElements.length; id++){
		for(var i = 0; i < listElements[id].length; i++){
			if(listElements[id][i].name.split(' ').length == 1 ||  inputBlock.value.split(' ').length > 1){
				var element = listElements[id][i].name.split('').slice(0,inputBlock.value.length).join('');
				element = element.toUpperCase()[0] + element.slice(1);
				
				var string = inputBlock.value.toUpperCase()[0] + inputBlock.value.slice(1);
				if(element == string){
					var option = dropdownOptionClone.cloneNode(true);
					option.style.display = "";
					option.children[0].setAttribute('name', returnTableType(listElements[id]));
					option.children[0].id = returnTableType(listElements[id]) + "_" + listElements[id][i].id;
					option.children[0].value = listElements[id][i].name;
					dropdownOptions.appendChild(option);
					
					option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
				}	
			}
			else{
				var elements = listElements[id][i].name.split(' ');
				var string = inputBlock.value.toUpperCase()[0] + inputBlock.value.slice(1);
				
				for(var k = 0; k < elements.length; k++){
					var element = elements[k].split('').slice(0,inputBlock.value.length).join('');
					element = element.toUpperCase()[0] + element.slice(1);
	
					if(element == string){
						var option = dropdownOptionClone.cloneNode(true);
						option.style.display = "";
						option.children[0].setAttribute('name', returnTableType(listElements[id]));
						option.children[0].id = returnTableType(listElements[id]) + "_" + listElements[id][i].id;
						option.children[0].value = listElements[id][i].name;
						dropdownOptions.appendChild(option);
						
						option.children[0].addEventListener("click", function(){addResultOption(this.id, idRow)});
					}
				}
			}
		}
	}
	if(dropdownOptions.children.length == 1){
		var option = dropdownOptionClone.cloneNode(true);
		option.style.display = "";
		option.children[0].value = "Ничего не найдено!";
		dropdownOptions.appendChild(option);
	}
	
}
//Добавление в список результатов
function addResultOption(elenentid, idRow){//check
	var elementid = document.getElementById(elenentid);
	var inputBlock = document.getElementById("clsInput_test_" + idRow);
	var main = inputBlock.parentNode.parentNode.parentNode;
	var classifierInpurResultRow = main.children[0].children[0];
	var option = elementid;
	var object = document.createElement("div");
	object.classList.add("wordElement");
	object.id = "result_" + option.id;
	object.textContent = option.value;
	object.addEventListener("click", function(){
		if(elementid.id.split("_")[1] = "product"){
			removeProductInfo(idRow)
		}
		this.remove();
		StartInput(idRow);
		changeClassifier(idRow);
	});
	classifierInpurResultRow.appendChild(object);
	sortResultBlock(idRow);
	changeClassifier(idRow);
	
	if(elementid.getAttribute("name") == "product"){
		addProductInfo(elementid, idRow);
	}
	
	document.getElementById("clsInput_test_" + idRow).focus();
	document.getElementById("clsInput_test_" + idRow).value="";
}
function searchid(idRow){//check
	return function e(){
		var addOption = document.getElementById('addOption_' + idRow);
		var main = addOption.parentNode.parentNode.parentNode;
		var clsDropdown = main.children[2].id;
		addCustomOption(idRow);
	}
}
function addCustomOption(idRow){	
	var dropdown = document.getElementById('clsDropdown_' + idRow);
	var main = dropdown.parentNode;
	var classifierInpurResult = main.children[0].children[0].id;
	var clsInput_test = main.children[1].children[0].children[0].id;
	var cls = document.getElementById(clsInput_test);
	if(dropdown.style.display != "none" && cls.value != ""){
		var object = document.createElement("div");
		object.classList.add("wordElement");
		object.textContent = cls.value;
		object.addEventListener("click", function(){
			this.remove();
			StartInput(idRow);
			changeClassifier(idRow);
		});
		document.getElementById(classifierInpurResult).appendChild(object);
		sortResultBlock(idRow);
		changeClassifier(idRow);
	}
	ShowDropdown(idRow);
}
//Сортировка результатов
function sortResultBlock(idRow){//check
	var resultBlock = document.getElementById('clsInputResultBlock_' + idRow);
	var keyList = ["product", "weed", "productType", "weedClass", "discription", "parts", "status", "color", "customeOption"];
	
	for(var i = 0; i < resultBlock.children.length; i++){
		var type = resultBlock.children[i].id != "" ? resultBlock.children[i].id.split("_")[1] : "customeOption";
		for(var k = 0; k < keyList.length; k++){
			if(type == keyList[k])
				resultBlock.children[i].setAttribute('name', k);
		}
	}	
	[].map.call( resultBlock.children, Object ).sort( function ( a, b ) {
		return +a.getAttribute("name") - +b.getAttribute("name");
	}).forEach( function ( elem ) {resultBlock.appendChild( elem )}); 
	
}
function addProductInfo(product_id, idRow){
	var infoBlockElement = document.getElementById("infoBlock_" + idRow);
	var cloneOptionInfo = infoBlockElement.children[0].cloneNode(true);
	var infoTitle = document.getElementById("infoTitle_" + idRow);
	var ID = product_id.id.split("_")[1];
	//ссылка на википедию
	cloneOptionInfo.style.display = "";
	cloneOptionInfo.children[0].value = "WIKI";
	cloneOptionInfo.children[0].addEventListener("click", function(){
		window.open(list_product[ID].wikilink)
	});
	infoBlockElement.appendChild(cloneOptionInfo);
	//ссылки на госты
	var ID_GOSTS_LIST = list_product[ID].purpose_seed.concat(list_product[ID].purpose_fodder, list_product[ID].purpose_raw, list_product[ID].purpose_export, list_product[ID].purpose_groats)
	
	for(var i = 0; i < list_product[ID].purpose_seed.length; i++){
		if(list_product[ID].purpose_seed[i] != "-"){
			var cloneOptionInfo = infoBlockElement.children[0].cloneNode(true);
			var id = list_product[ID].purpose_seed[i];
			
			cloneOptionInfo.style.display = "";
			cloneOptionInfo.children[0].value = list_GOST[id-1].gostName;
			cloneOptionInfo.children[0].addEventListener("click", function(){
				window.open(list_GOST[id-1].link);
			});
			infoBlockElement.appendChild(cloneOptionInfo);
		}
	}
	for(var i = 0; i < list_product[ID].purpose_fodder.length; i++){
		if(list_product[ID].purpose_fodder[i] != "-"){
			var cloneOptionInfo = infoBlockElement.children[0].cloneNode(true);
			var id = list_product[ID].purpose_fodder[i];
			
			cloneOptionInfo.style.display = "";
			cloneOptionInfo.children[0].value = list_GOST[id-1].gostName;
			cloneOptionInfo.children[0].addEventListener("click", function(){
				window.open(list_GOST[id-1].link);
			});
			infoBlockElement.appendChild(cloneOptionInfo);
		}
	}
	for(var i = 0; i < list_product[ID].purpose_raw.length; i++){
		if(list_product[ID].purpose_raw[i] != "-"){
			var cloneOptionInfo = infoBlockElement.children[0].cloneNode(true);
			var id = list_product[ID].purpose_raw[i];
			
			cloneOptionInfo.style.display = "";
			cloneOptionInfo.children[0].value = list_GOST[id-1].gostName;
			cloneOptionInfo.children[0].addEventListener("click", function(){
				window.open(list_GOST[id-1].link);
			});
			infoBlockElement.appendChild(cloneOptionInfo);
		}
	}
	for(var i = 0; i < list_product[ID].purpose_export.length; i++){
		if(list_product[ID].purpose_export[i] != "-"){
			var cloneOptionInfo = infoBlockElement.children[0].cloneNode(true);
			var id = list_product[ID].purpose_export[i];
			
			cloneOptionInfo.style.display = "";
			cloneOptionInfo.children[0].value = list_GOST[id-1].gostName;
			cloneOptionInfo.children[0].addEventListener("click", function(){
				window.open(list_GOST[id-1].link);
			});
			infoBlockElement.appendChild(cloneOptionInfo);
		}
	}
	for(var i = 0; i < list_product[ID].purpose_groats.length; i++){
		if(list_product[ID].purpose_groats[i] != "-"){
			var cloneOptionInfo = infoBlockElement.children[0].cloneNode(true);
			var id = list_product[ID].purpose_groats[i];
			
			cloneOptionInfo.style.display = "";
			cloneOptionInfo.children[0].value = list_GOST[id-1].gostName;
			cloneOptionInfo.children[0].addEventListener("click", function(){
				window.open(list_GOST[id-1].link);
			});
			infoBlockElement.appendChild(cloneOptionInfo);
		}
	}	
	if(infoBlockElement.children.length != 0)
		infoTitle.style.display = "";
}
function removeProductInfo(idRow){//check
	var inputBlock = document.getElementById('clsInput_test_' + idRow);
	var main = inputBlock.parentNode.parentNode.parentNode;
	var infoTitle = main.children[2].children[1].id;
	var infoBlock = main.children[2].children[2].id;
	document.getElementById(infoTitle).style.display = "none";
	for(var i = document.getElementById(infoBlock).children.length - 1; i > 0; i--){
		document.getElementById(infoBlock).children[i].remove();
	}
}
function resultTextView(clsInput_testRow, classifierInpurResultElement){//check
	clsInput_testRow.value = "";
	for(var i = 0; i < classifierInpurResultElement.children.length; i++){
		clsInput_testRow.value = clsInput_testRow.value != "" ? clsInput_testRow.value + " " + classifierInpurResultElement.children[i].textContent : classifierInpurResultElement.children[i].textContent;
	}
}
function checkResultOption(list, listElement){//check
	var index = list.indexOf(listElement);
	if(index > -1)
		list.splice(index, 1);
	
	return list;
}
//Изменение параметров классификатора
function changeClassifier(idRow){//check
	//Дефолтная установка
	var classifier = componentElementClassifier;
	var resultBlock = document.getElementById('clsInputResultBlock_' + idRow);
	var classifierInpurResult = document.getElementById('classifierInpurResult_' + idRow);
	classifier.classifierType = 0;
	classifier.classifierProduct.useADD = false;
	classifier.classifierProduct.mainOptions.industryID = 0;
	classifier.classifierProduct.addCustomOption = "";
	classifier.classifierWeed.useADD = false;
	classifier.classifierWeed.mainOptions.industryID = 0;
	classifier.classifierWeed.addCustomOption = "";
	//Основные установки
	for(var i = 0; i < resultBlock.children[0].children.length; i++){
		var resultType = resultBlock.children[0].children[i].id != "" ? resultBlock.children[0].children[i].id.split("_")[1] : "customeOption";
		var resultID = classifierInpurResult.children[i].id.split('_')[2];
		switch(resultType){
			case "product":
				classifier.classifierType = 0;
				classifier.classifierProduct.mainOptions.productID = list_product[resultID].id_product;
				classifier.classifierProduct.mainOptions.groupProductID = list_product[resultID].id_productGroup;
				break;
			case "weed":
				classifier.classifierType = 1;
				classifier.classifierProduct.classifierWeed.weedNameID = list_weed[resultID].weedNameID;
				classifier.classifierWeed.mainOptions.classWeedID = list_weed[resultID].id_class;
				break;
			case "productType":
				classifier.classifierType = 0;
				classifier.classifierProduct.mainOptions.productTypeID = list_productType[resultID].id_productType;
				break;
			case "weedClass":
				classifier.classifierType = 1;
				classifier.classifierWeed.mainOptions.classWeedID = list_weed[resultID].id_class;
				classifier.classifierWeed.mainOptions.categoryID = list_weed[resultID].id_category;
				break;
			case "discription":
				classifier.classifierProduct.mainOptions.descriptionID = list_descriptionSeed[resultID].id_description;
				break;
			case "parts":
				classifier.classifierProduct.mainOptions.partsID = list_productPart[resultID].id_number;
				break;
			case "status":
				classifier.classifierProduct.mainOptions.statusID = list_productStatus[resultID].id_number;
				break;
			case "color":
				classifier.classifierWeed.mainOptions.colorID = list_productColor[resultID].id_number;
				break;
			case "customeOption":
				if (classifier.classifierType == 0){
					classifier.classifierProduct.addCustomOption += resultBlock.children[i].textContent + ", ";
				}
				else{
					classifier.classifierWeed.addCustomOption += resultBlock.children[i].textContent + ", ";
				}
				break;
		}
	}
}
//дополнительная функция для кнопочки.
function checkboxOption(elementID, bool){
	var option = document.getElementById(elementID);
	if(option != null){
		var checkbox = option.parentNode.children[1].children[0];
		checkbox.checked = bool;
	}
}
function ShowDropdown(idRow){
	return function e(){
		HideAllDropdown();
		var dropdown = document.getElementById('clsDropdown_' + idRow);
		var clsInput_test = document.getElementById('clsInput_test_' + idRow);
		var otherCheckbox = document.getElementById('addOption_' + idRow);
		var classifierInpurResult = document.getElementById('classifierInpurResult_' + idRow);
		var clsInputResultBlock = document.getElementById('clsInputResultBlock_' + idRow);
		var lockBlock = document.getElementById('lockBlock');

		dropdown.style.display="flex";
		clsInput_test.value = ""
		classifierInpurResult.style.display="flex";
		clsInputResultBlock.style.display="flex";
		otherCheckbox.style.display="flex";
		lockBlock.style.display = "none";
		capacitySlider.style.display = "none";

		StartInput(idRow);
	}
}
function HideDropdown(idElement){
	return function e(){
		var button = document.getElementById(idElement);
		var main = button.parentNode.parentNode.parentNode;
		var dropdown = main.children[2];	
		var otherCheckbox = main.children[1].children[0].children[1];
		var clsInput_testRow = main.children[1].children[0].children[0];
		var classifierInpurResultElement = main.children[0].children[0];
		var lockBlock = document.getElementById('lockBlock');
		dropdown.style.display = "none";	
		resultTextView(clsInput_testRow, classifierInpurResultElement);
		classifierInpurResultElement.style.display="none";
		main.children[0].style.display="none";
		otherCheckbox.style.display="none";
		lockBlock.style.display = 'none';
		capacitySlider.style.display = "none";
	}
}
//Работа с интерфейсом весовых категорий
function ShowUpsertDropdown(element){
	
	var parent = element.parentNode.parentNode.parentNode;

	if(parent.children[0].style.width != '188px'){
		if(parent.id.split('_')[1] == '1'){
			var input = document.getElementById('massInput_' + parent.id.split('_')[1] +'_1');
			input.click();
			var massInputElement = document.getElementById(input.id);
			var main = massInputElement.parentNode.parentNode;
			var massInputResultBlockEl = main.children[1];
			var massInputBlockEl = main.children[0];
			var moreTitleEl = main.children[2];
			var massDropdownEl = main.children[3].children[0];

			massInputResultBlockEl.style.display = "flex";
			massInputBlockEl.style.display = "none";		
			massDropdownEl.style.display = "none";
			moreTitleEl.style.display = "none";			
		}
		else{
			var input = document.getElementById('MassInput_' + parent.id.split('_')[1] +'_1');
			input.click();
			var massInputElement = document.getElementById(input.id);
			var main = massInputElement.parentNode.parentNode;
			var massInputResultBlockEl = main.children[1];
			var massInputBlockEl = main.children[0];
			var moreTitleEl = main.children[2];
			var massDropdownEl = main.children[3].children[0];

			massInputResultBlockEl.style.display = "flex";
			massInputBlockEl.style.display = "none";		
			massDropdownEl.style.display = "none";
			moreTitleEl.style.display = "none";
		}	
	}	
	element.focus();
}
function ShowMassDropdown(elementID){
	return function e(){
		HideAllDropdown();
		var massInputElement = document.getElementById(elementID);
		var main = massInputElement.parentNode.parentNode;
		var massInputResultBlockEl = main.children[1];
		var massInputBlockEl = main.children[0];
		var moreTitleEl = main.children[2];
		var massDropdownEl = main.children[3].children[0];
		var fractionMainValues = document.getElementById('fractionMainValues_' + elementID.split('_')[1]);
		var fractionSource = document.getElementById('fractionSource_' + elementID.split('_')[1]);
		var lockBlock = document.getElementById('lockBlock');
		var fractionLockValue = document.getElementById('fractionLockValue_' + elementID.split('_')[1]);

		massInputResultBlockEl.style.display = "none";
		massInputBlockEl.style.display = "flex";		
		moreTitleEl.style.display = "flex";
		massDropdownEl.style.display = "flex";
		lockBlock.style.display = "flex";
		capacitySlider.style.display = "flex";
		
		main.children[0].children[0].children[0].focus();		
		main.style.width="190px";
		fractionSource.style.width="190px";
		fractionSource.children[0].style.width="190px";
		fractionSource.children[0].style.height="190px";
		fractionSource.children[1].style.width="190px";
		fractionLockValue.children[0].style.width="190px";
		fractionLockValue.children[0].children[0].style.display="none";
		fractionLockValue.children[0].children[1].style.display="flex";
		for(var i = 0; i< fractionMainValues.children.length; i++){
			fractionMainValues.children[i].style.width="188px";
		}
		if(massInputBlockEl.style.display = "flex"){
			var numberBlock = massInputElement.id.split('_')[1];
			var numberRow = massInputElement.id.split('_')[2];
			switch(numberBlock){
				case '1':
					var massInputResultBlockEl2 = document.getElementById(massInputResultBlockEl.id.split('_')[0] + '_2_' + numberRow);
					var massInputBlockEl2 = document.getElementById(massInputBlockEl.id.split('_')[0] + '_2_' + numberRow);
					var moreTitleEl2 = document.getElementById(moreTitleEl.id.split('_')[0] + '_2_' + numberRow);
					var massDropdownEl2 = document.getElementById(massDropdownEl.id.split('_')[0] + '_2_' + numberRow);

					var massInputResultBlockEl3 = document.getElementById(massInputResultBlockEl.id.split('_')[0] + '_3_' + numberRow);
					var massInputBlockEl3 = document.getElementById(massInputBlockEl.id.split('_')[0] + '_3_' + numberRow);
					var moreTitleEl3 = document.getElementById(moreTitleEl.id.split('_')[0] + '_3_' + numberRow);
					var massDropdownEl3 = document.getElementById(massDropdownEl.id.split('_')[0] + '_3_' + numberRow);

					var main2 = document.getElementById(main.id.split('_')[0] + '_2_' + numberRow);
					var main3 = document.getElementById(main.id.split('_')[0] + '_3_' + numberRow);

					var fractionMainValues2 = document.getElementById(fractionMainValues.id.split('_')[0] + '_2');
					var fractionMainValues3 = document.getElementById(fractionMainValues.id.split('_')[0] + '_3');
					var fractionSource2 = document.getElementById(fractionSource.id.split('_')[0] + '_2');
					var fractionSource3 = document.getElementById(fractionSource.id.split('_')[0] + '_3');
					
					var fractionLockValue2 = document.getElementById(fractionLockValue.id.split('_')[0] + '_2');
					var fractionLockValue3 = document.getElementById(fractionLockValue.id.split('_')[0] + '_3');
					

					massInputResultBlockEl2.style.display = "flex";
					massInputBlockEl2.style.display = "none";
					massDropdownEl2.style.display = "none";
					moreTitleEl2.style.display = "none";

					massInputResultBlockEl3.style.display = "flex";
					massInputBlockEl3.style.display = "none";
					massDropdownEl3.style.display = "none";
					moreTitleEl3.style.display = "none";

					main2.style.width="90px";
					main3.style.width="90px";

					fractionSource2.style.width="90px";
					fractionSource2.children[0].style.width="98px";
					fractionSource2.children[0].style.height="98px";
					fractionSource2.children[1].style.width="90px";
					fractionSource3.style.width="90px";
					fractionSource3.children[0].style.width="98px";
					fractionSource3.children[0].style.height="98px";
					fractionSource3.children[1].style.width="90px";					
					fractionLockValue2.children[0].children[0].style.display="flex";
					fractionLockValue2.children[0].children[1].style.display="none";
					fractionLockValue3.children[0].children[0].style.display="flex";
					fractionLockValue3.children[0].children[1].style.display="none";
					for(var i = 0; i< fractionMainValues2.children.length; i++){
						fractionMainValues2.children[i].style.width="";
					}
					for(var i = 0; i< fractionMainValues3.children.length; i++){
						fractionMainValues3.children[i].style.width="";
					}
					break;
				case '2':
					var massInputResultBlockEl2 = document.getElementById(massInputResultBlockEl.id.split('_')[0] + '_1_' + numberRow);
					var massInputBlockEl2 = document.getElementById(massInputBlockEl.id.split('_')[0] + '_1_' + numberRow);
					var moreTitleEl2 = document.getElementById(moreTitleEl.id.split('_')[0] + '_1_' + numberRow);
					var massDropdownEl2 = document.getElementById(massDropdownEl.id.split('_')[0] + '_1_' + numberRow);

					var massInputResultBlockEl3 = document.getElementById(massInputResultBlockEl.id.split('_')[0] + '_3_' + numberRow);
					var massInputBlockEl3 = document.getElementById(massInputBlockEl.id.split('_')[0] + '_3_' + numberRow);
					var moreTitleEl3 = document.getElementById(moreTitleEl.id.split('_')[0] + '_3_' + numberRow);
					var massDropdownEl3 = document.getElementById(massDropdownEl.id.split('_')[0] + '_3_' + numberRow);

					var main2 = document.getElementById(main.id.split('_')[0] + '_1_' + numberRow);
					var main3 = document.getElementById(main.id.split('_')[0] + '_3_' + numberRow);

					var fractionMainValues2 = document.getElementById(fractionMainValues.id.split('_')[0] + '_1');
					var fractionMainValues3 = document.getElementById(fractionMainValues.id.split('_')[0] + '_3');
					var fractionSource2 = document.getElementById(fractionSource.id.split('_')[0] + '_1');
					var fractionSource3 = document.getElementById(fractionSource.id.split('_')[0] + '_3');
					var fractionLockValue2 = document.getElementById(fractionLockValue.id.split('_')[0] + '_1');
					var fractionLockValue3 = document.getElementById(fractionLockValue.id.split('_')[0] + '_3');

					massInputResultBlockEl2.style.display = "flex";
					massInputBlockEl2.style.display = "none";
					massDropdownEl2.style.display = "none";
					moreTitleEl2.style.display = "none";

					massInputResultBlockEl3.style.display = "flex";
					massInputBlockEl3.style.display = "none";
					massDropdownEl3.style.display = "none";
					moreTitleEl3.style.display = "none";

					main2.style.width="80px";
					main3.style.width="80px";

					fractionSource2.style.width="86px";
					fractionSource2.children[0].style.width="98px";
					fractionSource2.children[0].style.height="98px";
					fractionSource2.children[1].style.width="";
					fractionSource3.style.width="86px";
					fractionSource3.children[0].style.width="98px";
					fractionSource3.children[0].style.height="98px";
					fractionSource3.children[1].style.width="";
					fractionLockValue2.children[0].children[0].style.display="flex";
					fractionLockValue2.children[0].children[1].style.display="none";
					fractionLockValue3.children[0].children[0].style.display="flex";
					fractionLockValue3.children[0].children[1].style.display="none";
					for(var i = 0; i< fractionMainValues2.children.length; i++){
						fractionMainValues2.children[i].style.width="";
					}
					for(var i = 0; i< fractionMainValues3.children.length; i++){
						fractionMainValues3.children[i].style.width="";
					}
					break;
				case '3':
					var massInputResultBlockEl2 = document.getElementById(massInputResultBlockEl.id.split('_')[0] + '_2_' + numberRow);
					var massInputBlockEl2 = document.getElementById(massInputBlockEl.id.split('_')[0] + '_2_' + numberRow);
					var moreTitleEl2 = document.getElementById(moreTitleEl.id.split('_')[0] + '_2_' + numberRow);
					var massDropdownEl2 = document.getElementById(massDropdownEl.id.split('_')[0] + '_2_' + numberRow);

					var massInputResultBlockEl3 = document.getElementById(massInputResultBlockEl.id.split('_')[0] + '_1_' + numberRow);
					var massInputBlockEl3 = document.getElementById(massInputBlockEl.id.split('_')[0] + '_1_' + numberRow);
					var moreTitleEl3 = document.getElementById(moreTitleEl.id.split('_')[0] + '_1_' + numberRow);
					var massDropdownEl3 = document.getElementById(massDropdownEl.id.split('_')[0] + '_1_' + numberRow);

					var main2 = document.getElementById(main.id.split('_')[0] + '_2_' + numberRow);
					var main3 = document.getElementById(main.id.split('_')[0] + '_1_' + numberRow);

					var fractionMainValues2 = document.getElementById(fractionMainValues.id.split('_')[0] + '_2');
					var fractionMainValues3 = document.getElementById(fractionMainValues.id.split('_')[0] + '_1');
					var fractionSource2 = document.getElementById(fractionSource.id.split('_')[0] + '_2');
					var fractionSource3 = document.getElementById(fractionSource.id.split('_')[0] + '_1');
					var fractionLockValue2 = document.getElementById(fractionLockValue.id.split('_')[0] + '_2');
					var fractionLockValue3 = document.getElementById(fractionLockValue.id.split('_')[0] + '_1');

					massInputResultBlockEl2.style.display = "flex";
					massInputBlockEl2.style.display = "none";
					massDropdownEl2.style.display = "none";
					moreTitleEl2.style.display = "none";

					massInputResultBlockEl3.style.display = "flex";
					massInputBlockEl3.style.display = "none";
					massDropdownEl3.style.display = "none";
					moreTitleEl3.style.display = "none";

					main2.style.width="80px";
					main3.style.width="80px";

					fractionSource2.style.width="86px";
					fractionSource2.children[0].style.width="98px";
					fractionSource2.children[0].style.height="98px";
					fractionSource2.children[1].style.width="";
					fractionSource3.style.width="86px";
					fractionSource3.children[0].style.width="98px";
					fractionSource3.children[0].style.height="98px";
					fractionSource3.children[1].style.width="";
					fractionLockValue2.children[0].children[0].style.display="flex";
					fractionLockValue2.children[0].children[1].style.display="none";
					fractionLockValue3.children[0].children[0].style.display="flex";
					fractionLockValue3.children[0].children[1].style.display="none";
					for(var i = 0; i< fractionMainValues2.children.length; i++){
						fractionMainValues2.children[i].style.width="";
					}
					for(var i = 0; i< fractionMainValues3.children.length; i++){
						fractionMainValues3.children[i].style.width="";
					}
					break;
			}
			for (var k = 1; k< rows.children.length; k++){
				rows.children[k].children[0].children[0].children[Number(numberBlock)+1].style.width = '184px';
			}		
		}
		
		GetLockSustate(elementID.split('_')[1]);
	}
}
function HideMassDropdown(elementID){
	return function e(){
		HideAllDropdown();
		var controlButton = document.getElementById(elementID);
		var main = controlButton.parentNode.parentNode;
		var massInputBlockEl = main.children[0];
		var massInputResultBlockEl = main.children[1];
		var moreTitleEl = main.children[2];
		var massDropdownEl = main.children[3].children[0];
		var fractionMainValues = document.getElementById('fractionMainValues_' + elementID.split('_')[1]);
		var fractionSource = document.getElementById('fractionSource_' + elementID.split('_')[1]);
		var lockBlock = document.getElementById('lockBlock');
		var fractionLockValue = document.getElementById('fractionLockValue_' + elementID.split('_')[1]);

		massInputResultBlockEl.style.display = "flex";
		massInputBlockEl.style.display = "none";		
		massDropdownEl.style.display = "none";
		moreTitleEl.style.display = "none";
		lockBlock.style.display = 'none';
		capacitySlider.style.display = "none";
				
		main.style.width="80px";
		fractionSource.style.width="86px";
		fractionSource.children[0].style.width="128px";
		fractionSource.children[0].style.height="128px";
		fractionSource.children[1].style.width="";
		fractionLockValue.children[0].style.width="";
		fractionLockValue.children[0].children[0].style.display="flex";
		fractionLockValue.children[0].children[1].style.display="none";
		for(var i = 0; i< fractionMainValues.children.length; i++){
			fractionMainValues.children[i].style.width="";
		}
		
	}
}

// Функция для скрытия всех блоков-параметров перед изменением стией и размеров 
	// скрытие всех боков-параметров и полей ввода
function HideAllDropdown(){	
	for (var i= 1; i<= 3; i++){
		var fractionSource = document.getElementById('fractionSource_' + i);
		var fractionMainValues = document.getElementById('fractionMainValues_' + i);
		var fractionLockValue = document.getElementById('fractionLockValue_' + i);
		fractionSource.style.width="86px";
		fractionSource.children[0].style.width="128px";
		fractionSource.children[0].style.height="128px";
		fractionSource.children[1].style.width="";
		fractionLockValue.children[0].style.width="";
		fractionLockValue.children[0].children[0].style.display="flex";
		fractionLockValue.children[0].children[1].style.display="none";	
		lockBlock.style.display = "none";
		capacitySlider.style.display = "none";
		for(var k = 0; k< fractionMainValues.children.length; k++){
			fractionMainValues.children[k].style.width="";
		}
	}
	for (var i = 1; i< rows.children.length; i++){
		// скрытие поисковых строк
		var clsInput_testRow = document.getElementById(rows.children[i].children[0].children[0].children[1].children[1].children[0].children[0].id);
		var classifierInpurResultElement = document.getElementById(rows.children[i].children[0].children[0].children[1].children[0].children[0].id);
		rows.children[i].children[0].children[0].children[1].children[2].style.display = 'none';
		resultTextView(clsInput_testRow, classifierInpurResultElement);
		rows.children[i].children[0].children[0].children[1].children[0].children[0].style.display = 'none';
		rows.children[i].children[0].children[0].children[1].children[0].style.display = 'none';
		rows.children[i].children[0].children[0].children[2].children[0].style.display = 'none';
		rows.children[i].children[0].children[0].children[1].children[1].children[0].children[1].style.display = 'none';
		// скрытие параметров фракций
		rows.children[i].children[0].children[0].children[2].children[2].style.display = 'none';
		rows.children[i].children[0].children[0].children[2].children[3].style.display = 'none';
		rows.children[i].children[0].children[0].children[2].children[1].style.display = 'flex';
		rows.children[i].children[0].children[0].children[2].style.width = '80px';
		rows.children[i].children[0].children[0].children[3].children[0].style.display = 'none';
		rows.children[i].children[0].children[0].children[3].children[2].style.display = 'none';
		rows.children[i].children[0].children[0].children[3].children[3].style.display = 'none';
		rows.children[i].children[0].children[0].children[3].children[1].style.display = 'flex';
		rows.children[i].children[0].children[0].children[3].style.width = '80px';
		rows.children[i].children[0].children[0].children[4].children[0].style.display = 'none';
		rows.children[i].children[0].children[0].children[4].children[2].style.display = 'none';
		rows.children[i].children[0].children[0].children[4].children[3].style.display = 'none';
		rows.children[i].children[0].children[0].children[4].children[1].style.display = 'flex';
		rows.children[i].children[0].children[0].children[4].style.width = '80px';		
	}
} 
function changeMassValue(mass, input){
	return function e(){
		var massDropdown = document.getElementById(mass);
		var massInputBlock = document.getElementById(input);
		var dropdownElements = massDropdown.children[0].children;
		for(var i = 0; i < dropdownElements.length; i++){
			if(!dropdownElements[i].children[0].readOnly){
				dropdownElements[i].children[0].value = massInputBlock.children[0].children[0].value; // В последствии обернуть в определенную функцию
				var evt = document.createEvent("HTMLEvents");
				evt.initEvent("change", false, true);
				dropdownElements[i].dispatchEvent(evt);
			}
		}
	}
}
function ShowDeleteButton(elementID){
	return function e(){
		var thisElement = document.getElementById(elementID);
		thisElement.children[1].style.display="none";
		thisElement.children[2].style.display="flex";
	}	
}
function HideDeleteButton(elementID){
	return function e(){
		var thisElement = document.getElementById(elementID);
		thisElement.children[1].style.display="flex";
		thisElement.children[2].style.display="none";
	}
}
function photoBlock(idRow){
	return function e(){
		if (document.getElementById("photoBlock_" + idRow).style.display=="none"){
			document.getElementById("photoBlock_" + idRow).style.display="flex";
			document.getElementById("photoBlockButton_" + idRow).style.transform = "rotate(180deg)";
			document.getElementById("photoTitle_" + idRow).style.borderBottomWidth="0px"
			document.getElementById("photoTitle_" + idRow).style.marginBottom="8px";
		}else{
			document.getElementById("photoBlock_" + idRow).style.display="none";
			document.getElementById("photoBlockButton_" + idRow).style.transform = "rotate(0deg)";
			document.getElementById("photoTitle_" + idRow).style.borderBottomWidth="1px"
			document.getElementById("photoTitle_" + idRow).style.marginBottom="0px";
		}
	}
}
function infoBlock(idRow){
	return function e(){
		if (document.getElementById('infoBlock_' + idRow).style.display=="none"){
			document.getElementById('infoBlock_' + idRow).style.display="flex";
			document.getElementById('infoBlockButton_' + idRow).style.transform = "rotate(180deg)";
			document.getElementById('infoTitle_' + idRow).style.borderBottomWidth="0px"
			document.getElementById('infoTitle_' + idRow).style.marginBottom="8px";
		}else{
			document.getElementById('infoBlock_' + idRow).style.display="none";
			document.getElementById('infoBlockButton_' + idRow).style.transform = "rotate(0deg)";
			document.getElementById('infoTitle_' + idRow).style.borderBottomWidth="1px"
			document.getElementById('infoTitle_' + idRow).style.marginBottom="0px";
		}
	}
}
function moreBlock(more, mBtton, mTitle){
	return function e(){
		if (document.getElementById(more).style.display=="none"){
			document.getElementById(more).style.display="";
			document.getElementById(mBtton).style.transform = "rotate(180deg)";
			document.getElementById(mTitle).style.borderBottomWidth="0px"
			document.getElementById(mTitle).style.marginBottom="8px";
		}else{
			document.getElementById(more).style.display="none";
			document.getElementById(mBtton).style.transform = "rotate(0deg)";
			document.getElementById(mTitle).style.borderBottomWidth="1px"
			document.getElementById(mTitle).style.marginBottom="0px";
		}
	}
}

//Смена изображений Тоглов
function switchToggle(){
	var imgName = this.style.backgroundImage.split('/')[5].split('.')[0];	
	switch(imgName){
		case "calcOn":
			this.style.backgroundImage = "url(/static/TestClassifier/img/classifier/calcOff.png)";
			break;
		case "calcOff":
			this.style.backgroundImage = "url(/static/TestClassifier/img/classifier/calcOn.png)";
			break;
		case "impOff":
			this.style.backgroundImage = "url(/static/TestClassifier/img/classifier/impOn.png)";
			break;
		case "impOn":
			this.style.backgroundImage = "url(/static/TestClassifier/img/classifier/impOff.png)";
			break;
		case "accept":
			this.style.backgroundImage = "url(/static/TestClassifier/img/classifier/reject.png)";
			break;
		case "reject":
			this.style.backgroundImage = "url(/static/TestClassifier/img/classifier/accept.png)";
			break;
	}
	setupComponentToggles(this);
}
//Переключение допольных опций весов компонета
function switchDropdownMass(element){
	var elementl = document.getElementById(element);
	var sliderBlock = elementl.children[0];
	//Псевдофункция
	function e(){
		var selectRow = this.parentNode;
		var sliderBlock = selectRow.parentNode;
		
		if(selectRow.children[0].readOnly){
			for(var i = 0 ; i < sliderBlock.children.length; i++){
				sliderBlock.children[i].style.display = "none";
			}
			selectRow.style.display = "flex";
			selectRow.children[0].readOnly = false;
			selectRow.children[1].style.backgroundColor = "#ffb23f";
		}
		else {
			for(var i = 0 ; i < sliderBlock.children.length; i++){
				sliderBlock.children[i].style.display = "flex";
			}
			selectRow.children[0].readOnly = true;
			selectRow.children[1].style.backgroundColor = "#f1f1f1";
		}
	}
	//Добавление слушателя на элементы ниспадающего списка
	for(var i = 0; i < sliderBlock.children.length; i++){
		sliderBlock.children[i].children[1].addEventListener("click", e);
	}
	for(var i = 2; i <= 3; i++){
		var newID = "massDropdown" + '_' + i + '_' + element.split('_')[2];
		var elementl = document.getElementById(newID);
		var sliderBlock = elementl.children[0];
		//Псевдофункция
		function e(){
			var selectRow = this.parentNode;
			var sliderBlock = selectRow.parentNode;
			
			if(selectRow.children[0].readOnly){
				for(var i = 0 ; i < sliderBlock.children.length; i++){
					sliderBlock.children[i].style.display = "none";
				}
				selectRow.style.display = "flex";
				selectRow.children[0].readOnly = false;
				selectRow.children[1].style.backgroundColor = "#ffb23f";
			}
			else {
				for(var i = 0 ; i < sliderBlock.children.length; i++){
					sliderBlock.children[i].style.display = "flex";
				}
				selectRow.children[0].readOnly = true;
				selectRow.children[1].style.backgroundColor = "#f1f1f1";
			}
		}
		//Добавление слушателя на элементы ниспадающего списка
		for(var k = 0; k < sliderBlock.children.length; k++){
			sliderBlock.children[k].children[1].addEventListener("click", e);
		}
	}	
}

//добавление и удаление строк
function addrow(){
	HideAllDropdown();
	var row = mainRow.cloneNode(true);
	var idRow = Number(rows.children.length);
	row.style.display = 'flex';
	row.id = 'mainRow_' + idRow;
	row.children[0].children[0].children[0].id = 'rowNumberId_' + idRow;
	row.children[0].children[0].children[0].addEventListener('mouseenter', ShowDeleteButton('rowNumberId_' + idRow));
	row.children[0].children[0].children[0].addEventListener('mouseleave', HideDeleteButton('rowNumberId_' + idRow));
	row.children[0].children[0].children[0].children[0].children[0].id = 'photoComponent_' + idRow;
	row.children[0].children[0].children[0].children[1].id = 'componentNumber_00_' + idRow;
	row.children[0].children[0].children[0].children[1].textContent = idRow;
	row.children[0].children[0].children[0].children[2].id = 'deleteButton_00_' + idRow;
	row.children[0].children[0].children[0].children[2].addEventListener('click', removeRow('deleteButton_00_' + idRow));
	// classifier
	row.children[0].children[0].children[1].id = 'classifier_' + idRow;
	row.children[0].children[0].children[1].children[0].id = 'clsInputResultBlock_' + idRow;
	row.children[0].children[0].children[1].children[0].children[0].id = 'classifierInpurResult_' + idRow;
	row.children[0].children[0].children[1].children[0].children[1].children[0].id = 'controlButtonIdHide_' + idRow;
	row.children[0].children[0].children[1].children[0].children[1].children[0].addEventListener('click', HideDropdown('controlButtonIdHide_' + idRow));
	row.children[0].children[0].children[1].children[0].children[1].children[0].addEventListener('click', setupComponentName);
	row.children[0].children[0].children[1].children[1].children[0].children[0].id = 'clsInput_test_' + idRow;
	row.children[0].children[0].children[1].children[1].children[0].children[0].addEventListener('focus', ShowDropdown(idRow));
	row.children[0].children[0].children[1].children[1].children[0].children[0].addEventListener('input', StartInputListeners(idRow));
	row.children[0].children[0].children[1].children[1].children[0].children[1].id = 'addOption_' + idRow;
	row.children[0].children[0].children[1].children[1].children[0].children[1].addEventListener('click', searchid(idRow));
	row.children[0].children[0].children[1].children[2].id = 'clsDropdown_' + idRow;
	row.children[0].children[0].children[1].children[2].children[0].children[0].children[0].id = 'clsOption_0_' + idRow;
	row.children[0].children[0].children[1].children[2].children[1].id = 'infoTitle_' + idRow;
	row.children[0].children[0].children[1].children[2].children[1].children[1].id = 'infoBlockButton_' + idRow;
	row.children[0].children[0].children[1].children[2].children[1].children[1].addEventListener('click', infoBlock(idRow));
	row.children[0].children[0].children[1].children[2].children[2].id = 'infoBlock_' + idRow;
	row.children[0].children[0].children[1].children[2].children[3].id = 'photoTitle_' + idRow;
	row.children[0].children[0].children[1].children[2].children[3].children[1].id = 'photoBlockButton_' + idRow;
	row.children[0].children[0].children[1].children[2].children[3].children[1].addEventListener('click', photoBlock(idRow));
	row.children[0].children[0].children[1].children[2].children[4].id = 'photoBlock_' + idRow;
	// valueBlock	
	row.children[0].children[0].children[2].id = 'valueBlock_1_' + idRow;
	row.children[0].children[0].children[2].children[0].id = 'massInputBlock_1_' + idRow;
	row.children[0].children[0].children[2].children[0].children[0].children[0].addEventListener('change', changeMassValue('massDropdown_1_' + idRow, 'massInputBlock_1_' + idRow));
	row.children[0].children[0].children[2].children[0].children[4].id = 'controlButtonId_1_' + idRow;
	row.children[0].children[0].children[2].children[0].children[4].addEventListener('click', HideMassDropdown('controlButtonId_1_' + idRow));
	row.children[0].children[0].children[2].children[1].id = 'massInputResultBlock_1_' + idRow;
	row.children[0].children[0].children[2].children[1].children[0].id = 'massInput_1_' + idRow;
	row.children[0].children[0].children[2].children[1].children[0].addEventListener('click', ShowMassDropdown('massInput_1_' + idRow));
	row.children[0].children[0].children[2].children[2].id = 'moreTitle_1_' + idRow;
	row.children[0].children[0].children[2].children[2].children[1].id = 'moreBlockButton_' + idRow;
	row.children[0].children[0].children[2].children[2].children[1].addEventListener('click', moreBlock('moreBlock_' + idRow,'moreBlockButton_' + idRow , 'moreTitle_1_' + idRow));
	row.children[0].children[0].children[2].children[3].id = 'moreBlock_' + idRow;
	row.children[0].children[0].children[2].children[3].children[0].id = 'massDropdown_1_' + idRow;
	row.children[0].children[0].children[2].children[0].children[1].children[0].addEventListener("click", switchToggle);
	row.children[0].children[0].children[2].children[0].children[2].children[0].addEventListener("click", switchToggle);
	row.children[0].children[0].children[2].children[0].children[3].children[0].addEventListener("click", switchToggle);
	// valueBlock_2	
	row.children[0].children[0].children[3].id = 'valueBlock_2_' + idRow;
	row.children[0].children[0].children[3].children[0].id = 'massInputBlock_2_' + idRow;
	row.children[0].children[0].children[3].children[0].children[0].children[0].addEventListener('change', changeMassValue('massDropdown_2_' + idRow, 'massInputBlock_2_' + idRow));
	row.children[0].children[0].children[3].children[0].children[4].id = 'controlButtonId_2_' + idRow;
	row.children[0].children[0].children[3].children[0].children[4].addEventListener('click', HideMassDropdown('controlButtonId_2_' + idRow));
	row.children[0].children[0].children[3].children[1].id = 'massInputResultBlock_2_' + idRow;
	row.children[0].children[0].children[3].children[1].children[0].id = 'MassInput_2_' + idRow;
	row.children[0].children[0].children[3].children[1].children[0].addEventListener('click', ShowMassDropdown('MassInput_2_' + idRow));
	row.children[0].children[0].children[3].children[2].id = 'moreTitle_2_' + idRow;
	row.children[0].children[0].children[3].children[2].children[1].id = 'moreBlockButton_2_' + idRow;
	row.children[0].children[0].children[3].children[2].children[1].addEventListener('click', moreBlock('moreBlock_2_' + idRow,'moreBlockButton_2_' + idRow , 'moreTitle_2_' + idRow));
	row.children[0].children[0].children[3].children[3].id = 'moreBlock_2_' + idRow;
	row.children[0].children[0].children[3].children[3].children[0].id = 'massDropdown_2_' + idRow;
	row.children[0].children[0].children[3].children[0].children[1].children[0].addEventListener("click", switchToggle);
	row.children[0].children[0].children[3].children[0].children[2].children[0].addEventListener("click", switchToggle);
	row.children[0].children[0].children[3].children[0].children[3].children[0].addEventListener("click", switchToggle);
	// valueBlock_3	
	row.children[0].children[0].children[4].id = 'valueBlock_3_' + idRow;
	row.children[0].children[0].children[4].children[0].id = 'massInputBlock_3_' + idRow;
	row.children[0].children[0].children[4].children[0].children[0].children[0].addEventListener('change', changeMassValue('massDropdown_3_' + idRow, 'massInputBlock_3_' + idRow));
	row.children[0].children[0].children[4].children[0].children[4].id = 'controlButtonId_3_' + idRow;
	row.children[0].children[0].children[4].children[0].children[4].addEventListener('click', HideMassDropdown('controlButtonId_3_' + idRow));
	row.children[0].children[0].children[4].children[1].id = 'massInputResultBlock_3_' + idRow;
	row.children[0].children[0].children[4].children[1].children[0].id = 'MassInput_3_' + idRow;
	row.children[0].children[0].children[4].children[1].children[0].addEventListener('click', ShowMassDropdown('MassInput_3_' + idRow));
	row.children[0].children[0].children[4].children[2].id = 'moreTitle_3_' + idRow;
	row.children[0].children[0].children[4].children[2].children[1].id = 'moreBlockButton_3_' + idRow;
	row.children[0].children[0].children[4].children[2].children[1].addEventListener('click', moreBlock('moreBlock_3_' + idRow,'moreBlockButton_3_' + idRow , 'moreTitle_3_' + idRow));
	row.children[0].children[0].children[4].children[3].id = 'moreBlock_3_' + idRow;
	row.children[0].children[0].children[4].children[3].children[0].id = 'massDropdown_3_' + idRow;
	row.children[0].children[0].children[4].children[0].children[1].children[0].addEventListener("click", switchToggle);
	row.children[0].children[0].children[4].children[0].children[2].children[0].addEventListener("click", switchToggle);
	row.children[0].children[0].children[4].children[0].children[3].children[0].addEventListener("click", switchToggle);
	rows.appendChild(row);
	//Изначальное значение строк
	setupComponentRow();
	mathfComponentFunction('massDropdown_1_' + idRow);
	mathfComponentFunction('massDropdown_2_' + idRow);
	mathfComponentFunction('massDropdown_3_' + idRow);
	componentRow[idRow-1].component_name = document.getElementById("clsInput_test_"+idRow).placeholder;
	switch(String(idRow)){
		case'1':
			clsInput_test_1.placeholder = 'Продукт';
			componentRow[idRow-1].component_name = document.getElementById("clsInput_test_"+idRow).placeholder;
			break;
		case'2':
			clsInput_test_2.placeholder = 'Засоритель';
			componentRow[idRow-1].component_name = document.getElementById("clsInput_test_"+idRow).placeholder;
			document.getElementById('massInputBlock_1_2').children[3].children[0].click();
			document.getElementById('massInputBlock_2_2').children[3].children[0].click();
			document.getElementById('massInputBlock_3_2').children[3].children[0].click();
			break;
	}	
	switchDropdownMass('massDropdown_1_' + idRow);
	updateRemovedPercent();
}
function removeRow(remove){
	return function e(){
		var elementRemove = document.getElementById(remove).parentNode.parentNode.parentNode.parentNode.id;
		document.getElementById(elementRemove).remove();
		
		var idComponentRow = Number(elementRemove.split("_")[1]-1)
		componentRow.splice(idComponentRow, 1);
		refreshID();
		updateRemovedPercent();
	}
}
function clearEventListener(element){//это вспомогательный для очистки слушатеlей
	const clonedElement = element.cloneNode(true);
	element.replaceWith(clonedElement);
	return clonedElement;
}
function refreshListeners(idRow){
	for(var i = 1; i < rows.children.length;i++){
		var classifierInpurResult = document.getElementById('classifierInpurResult_'+i);
		// classifierInpurResult.addEventListener('click', addCustomOption(idRow));
		if(classifierInpurResult != null && classifierInpurResult.children.length != 0 ){
			for(var k = 0; k < classifierInpurResult.children.length; k++){
				classifierInpurResult.children[k].addEventListener("click", function(){
					this.remove();
					StartInput(idRow);
					changeClassifier(idRow);
				});
			}
		}
		
	}
}
function refreshID(){
	var rows = document.getElementById('rows');
	for(var i = 1; i < rows.children.length; i++){
		var idRow = i;
		var cloneRow = clearEventListener(rows.children[i]);
		
		cloneRow.id = 'mainRow_' + idRow;
		cloneRow.children[0].children[0].children[0].id = 'rowNumberId_' + idRow;
		cloneRow.children[0].children[0].children[0].addEventListener('mouseenter', ShowDeleteButton('rowNumberId_' + idRow));
		cloneRow.children[0].children[0].children[0].addEventListener('mouseleave', HideDeleteButton('rowNumberId_' + idRow));
		cloneRow.children[0].children[0].children[0].children[0].children[0].id = 'photoComponent_' + idRow;
		cloneRow.children[0].children[0].children[0].children[1].id = 'componentNumber_00_' + idRow;
		cloneRow.children[0].children[0].children[0].children[1].textContent = idRow;
		cloneRow.children[0].children[0].children[0].children[2].id = 'deleteButton_00_' + idRow;
		cloneRow.children[0].children[0].children[0].children[2].addEventListener('click', removeRow('deleteButton_00_' + idRow));
		// classifier
		cloneRow.children[0].children[0].children[1].id = 'classifier_' + idRow;
		cloneRow.children[0].children[0].children[1].children[0].id = 'clsInputResultBlock_' + idRow;
		cloneRow.children[0].children[0].children[1].children[0].children[0].id = 'classifierInpurResult_' + idRow;
		cloneRow.children[0].children[0].children[1].children[0].children[1].children[0].id = 'controlButtonIdHide_' + idRow;
		cloneRow.children[0].children[0].children[1].children[0].children[1].children[0].addEventListener('click', HideDropdown('controlButtonIdHide_' + idRow));
		cloneRow.children[0].children[0].children[1].children[0].children[1].children[0].addEventListener('click', setupComponentName);
		cloneRow.children[0].children[0].children[1].children[1].children[0].children[0].id = 'clsInput_test_' + idRow;
		cloneRow.children[0].children[0].children[1].children[1].children[0].children[0].addEventListener('focus', ShowDropdown(idRow));
		cloneRow.children[0].children[0].children[1].children[1].children[0].children[0].addEventListener('input', StartInputListeners(idRow));
		cloneRow.children[0].children[0].children[1].children[1].children[0].children[1].id = 'addOption_' + idRow;
		cloneRow.children[0].children[0].children[1].children[1].children[0].children[1].addEventListener('click', searchid(idRow));
		cloneRow.children[0].children[0].children[1].children[2].id = 'clsDropdown_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[0].children[0].children[0].id = 'clsOption_0_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[1].id = 'infoTitle_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[1].children[1].id = 'infoBlockButton_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[1].children[1].addEventListener('click', infoBlock(idRow));
		cloneRow.children[0].children[0].children[1].children[2].children[2].id = 'infoBlock_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[3].id = 'photoTitle_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[3].children[1].id = 'photoBlockButton_' + idRow;
		cloneRow.children[0].children[0].children[1].children[2].children[3].children[1].addEventListener('click', photoBlock(idRow));
		cloneRow.children[0].children[0].children[1].children[2].children[4].id = 'photoBlock_' + idRow;
		// valueBlock	
		cloneRow.children[0].children[0].children[2].id = 'valueBlock_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[0].id = 'massInputBlock_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[0].children[0].children[0].addEventListener('change', changeMassValue('massDropdown_1_' + idRow, 'massInputBlock_1_' + idRow));
		cloneRow.children[0].children[0].children[2].children[0].children[4].id = 'controlButtonId_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[0].children[4].addEventListener('click', HideMassDropdown('controlButtonId_1_' + idRow));
		cloneRow.children[0].children[0].children[2].children[1].id = 'massInputResultBlock_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[1].children[0].id = 'massInput_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[1].children[0].addEventListener('click', ShowMassDropdown('massInput_1_' + idRow));
		cloneRow.children[0].children[0].children[2].children[2].id = 'moreTitle_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[2].children[1].id = 'moreBlockButton_' + idRow;
		cloneRow.children[0].children[0].children[2].children[2].children[1].addEventListener('click', moreBlock('moreBlock_' + idRow,'moreBlockButton_' + idRow , 'moreTitle_1_' + idRow));
		cloneRow.children[0].children[0].children[2].children[3].id = 'moreBlock_' + idRow;
		cloneRow.children[0].children[0].children[2].children[3].children[0].id = 'massDropdown_1_' + idRow;
		cloneRow.children[0].children[0].children[2].children[0].children[1].children[0].addEventListener("click", switchToggle);
		cloneRow.children[0].children[0].children[2].children[0].children[2].children[0].addEventListener("click", switchToggle);
		cloneRow.children[0].children[0].children[2].children[0].children[3].children[0].addEventListener("click", switchToggle);
		mathfComponentFunction('massDropdown_1_' + idRow);
		// valueBlock_2	
		cloneRow.children[0].children[0].children[3].id = 'valueBlock_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[0].id = 'massInputBlock_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[0].children[0].children[0].addEventListener('change', changeMassValue('massDropdown_2_' + idRow, 'massInputBlock_2_' + idRow));
		cloneRow.children[0].children[0].children[3].children[0].children[4].id = 'controlButtonId_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[0].children[4].addEventListener('click', HideMassDropdown('controlButtonId_2_' + idRow));
		cloneRow.children[0].children[0].children[3].children[1].id = 'massInputResultBlock_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[1].children[0].id = 'MassInput_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[1].children[0].addEventListener('click', ShowMassDropdown('MassInput_2_' + idRow));
		cloneRow.children[0].children[0].children[3].children[2].id = 'moreTitle_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[2].children[1].id = 'moreBlockButton_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[2].children[1].addEventListener('click', moreBlock('moreBlock_2_' + idRow,'moreBlockButton_2_' + idRow , 'moreTitle_2_' + idRow));
		cloneRow.children[0].children[0].children[3].children[3].id = 'moreBlock_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[3].children[0].id = 'massDropdown_2_' + idRow;
		cloneRow.children[0].children[0].children[3].children[0].children[1].children[0].addEventListener("click", switchToggle);
		cloneRow.children[0].children[0].children[3].children[0].children[2].children[0].addEventListener("click", switchToggle);
		cloneRow.children[0].children[0].children[3].children[0].children[3].children[0].addEventListener("click", switchToggle);
		mathfComponentFunction('massDropdown_2_' + idRow);
		// valueBlock_3	
		cloneRow.children[0].children[0].children[4].id = 'valueBlock_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[0].id = 'massInputBlock_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[0].children[0].children[0].addEventListener('change', changeMassValue('massDropdown_3_' + idRow, 'massInputBlock_3_' + idRow));
		cloneRow.children[0].children[0].children[4].children[0].children[4].id = 'controlButtonId_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[0].children[4].addEventListener('click', HideMassDropdown('controlButtonId_3_' + idRow));
		cloneRow.children[0].children[0].children[4].children[1].id = 'massInputResultBlock_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[1].children[0].id = 'MassInput_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[1].children[0].addEventListener('click', ShowMassDropdown('MassInput_3_' + idRow));
		cloneRow.children[0].children[0].children[4].children[2].id = 'moreTitle_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[2].children[1].id = 'moreBlockButton_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[2].children[1].addEventListener('click', moreBlock('moreBlock_3_' + idRow,'moreBlockButton_3_' + idRow , 'moreTitle_3_' + idRow));
		cloneRow.children[0].children[0].children[4].children[3].id = 'moreBlock_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[3].children[0].id = 'massDropdown_3_' + idRow;
		cloneRow.children[0].children[0].children[4].children[0].children[1].children[0].addEventListener("click", switchToggle);
		cloneRow.children[0].children[0].children[4].children[0].children[2].children[0].addEventListener("click", switchToggle);
		cloneRow.children[0].children[0].children[4].children[0].children[3].children[0].addEventListener("click", switchToggle);
		mathfComponentFunction('massDropdown_3_' + idRow);
		switchDropdownMass('massDropdown_1_' + idRow);
		switch(String(idRow)){
			case'1':
				clsInput_test_1.placeholder = 'Продукт';
				break;
			case'2':
				clsInput_test_2.placeholder = 'Засоритель';
				document.getElementById('massInputBlock_1_2').children[3].children[0].click();
				document.getElementById('massInputBlock_2_2').children[3].children[0].click();
				document.getElementById('massInputBlock_3_2').children[3].children[0].click();
				break;
		}	
		refreshListeners(idRow);
		
	}
}
// ЭТО ГРАФИКИ
	
var maasPipChart;
var chartData =[50,50,50,50];

function updateData(){
	acceptFraction = document.getElementById('acceptFraction').value;
	weedFraction = document.getElementById('weedFraction').value;
	rejectFraction = document.getElementById('rejectFraction').value;
	productFraction = document.getElementById('productFraction').value;

	chartData = [acceptFraction,weedFraction,rejectFraction,productFraction];
	handler(chartData);
}
function handler(chartData){
	maasPipChart.data.datasets.forEach(dataset => {
	dataset.data = chartData;
	});
	maasPipChart.update();
}
function ewe(){
	var doughnut = document.getElementById('doughnut').getContext('2d');
	var economic = document.getElementById('economic').getContext('2d');

	
	// настройки графика экономики
	 economicChart = new Chart(economic,{
		type: "line",
		data:{
			labels:['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'],
			datasets: [{
			label: 'расходы',
			data: [0,0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			
			borderColor: 'rgb(65,74,91)',
			backgroundColor: 'rgba(65,74,91, .1)',
			fill: "start",
			
			  },
			{
			label: 'доходы',
			data: [0,0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			
			borderColor: 'rgb(238, 164, 31)',
			backgroundColor: 'rgba(238, 164, 31, .5)',
			fill: "start",
			},]
			  
		},
	
		});

	// настройки графика производительности
	 maasPipChart = new Chart(doughnut,{
		type: "doughnut",
		data:{
			labels:['Проход','Засоритель в проходе','Отбой','Продукт в отбое'],
			datasets: [{
				label: 'capacity',
				data: [82,3, 10, 5],
				backgroundColor: ['#3354a1','red','#414a5b','#eea41f'],
				borderWidth: [1,0,1,1],
				hoverOffset: 32,
				rotation: 120,
				radius: 160,
				offset:[0,0,20,20],
			  },]
		},
		options:{
			responsive: true,
			maintainAspectRatio: false,
			
			plugins: {
			legend: false,
			tooltip: false,
					 }
				}
		});
}
function testLable(label){
	 economicChart.data.labels = label;
	 economicChart.update();
}

function economicShowDeleteButton(elementID){
	return function e(){
		var thisElement = document.getElementById(elementID);
		thisElement.children[0].style.display="none";
		thisElement.children[1].style.display="flex";
	}	
}
function economicHideDeleteButton(elementID){
	return function e(){
		var thisElement = document.getElementById(elementID);
		thisElement.children[0].style.display="flex";
		thisElement.children[1].style.display="none";
	}
}
function economicRemoveRow(remove){
	return function e(){
		var elementNumber = Number(remove.split('_')[1]);
		var elementRemove = document.getElementById(remove).parentNode.parentNode.parentNode.id;
		document.getElementById(elementRemove).remove();
		economicRowData.elements.splice(elementNumber, 1);
		economicrefreshID();
	}
}
//добавление и удаление строк для графика
function addrowGraph(){	
	var row = economicComponent_0.cloneNode(true);
	var idRow = Number(economicMainRow.children.length);	

	row.style.display = 'flex';
	row.id = 'economicComponent_' + idRow;	
	row.children[0].children[0].id = 'economicRowNumber_' + idRow;
	row.children[0].children[0].addEventListener('mouseenter', economicShowDeleteButton('economicRowNumber_' + idRow));
	row.children[0].children[0].addEventListener('mouseleave', economicHideDeleteButton('economicRowNumber_' + idRow));
	row.children[0].children[0].children[0].id = 'economicComponentNumber_' + idRow;
	row.children[0].children[0].children[0].textContent = idRow;
	row.children[0].children[0].children[1].id = 'economicDeleteButton_' + idRow;
	row.children[0].children[0].children[1].addEventListener('click', economicRemoveRow('economicDeleteButton_' + idRow));
	row.children[0].children[0].children[1].addEventListener('click', refreshEconomicChart());

	// economicSumParametr 
	row.children[0].children[2].id = "economicSumParametr_" + idRow;
	row.children[0].children[2].children[1].children[0].children[0].id = 'economSumModelType_' + idRow;
	row.children[0].children[2].children[1].children[0].children[2].id = 'economSumParam_' + idRow;
	row.children[0].children[2].children[1].children[0].children[2].children[2].id = 'economFraction_' + idRow;
	row.children[0].children[2].children[1].children[0].children[2].children[3].id = 'economFractionMass_' + idRow;
	row.children[0].children[2].children[1].children[0].children[2].children[5].id = 'economPercentParam_' + idRow;
	row.children[0].children[2].children[1].children[0].children[2].children[5].children[1].id = 'economArticle_' + idRow;
	row.children[0].children[2].children[1].children[1].children[0].id = 'economicDateParameter_' + idRow;
	row.children[0].children[2].children[1].children[1].children[0].children[0].id = 'economDateModelType_' + idRow;
	row.children[0].children[2].children[1].children[1].children[0].children[2].id = 'economDateParam_' + idRow;
	row.children[0].children[2].children[1].children[1].children[0].children[4].id = 'economPeriodParam_' + idRow;
	row.children[0].children[2].children[1].children[1].children[0].children[6].id = 'economFixedDate_' + idRow;
	// row
	row.children[0].children[3].children[0].children[0].children[0].id = 'arrow_' + idRow;
	row.children[0].children[3].children[0].children[0].children[0].addEventListener("click", function () {
		economicRowData.elements[idRow].IncomeArrow = this.checked;
		refreshEconomicChart();
	});

	row.children[0].children[2].children[0].children[0].children[0].addEventListener("click", function () {
		fractionSumParametersView(idRow);
		setupSumParametrText(idRow);
		refreshEconomicChart();
	});
	row.children[0].children[2].children[0].children[1].children[0].addEventListener("click", function () {
		fractionSumParametersView(idRow);
		setupSumParametrText(idRow);
		refreshEconomicChart();
	});
	var economSumModelType = row.children[0].children[2].children[1].children[0].children[0];
	var economSumParam = row.children[0].children[2].children[1].children[0].children[2];
	var economFraction = row.children[0].children[2].children[1].children[0].children[2].children[2];
	var economFractionMass = row.children[0].children[2].children[1].children[0].children[2].children[3];
	var scrollBlockSumModelType = economSumModelType.children[0].children[0].children;
	var scrollBlockSumParam = economSumParam.children[0].children[0].children;
	var scrollBlockFraction = economFraction.children[0].children[0].children;
	var scrollBlockFractionMass = economFractionMass.children[0].children[0].children;

	scrollBlockSumModelType[0].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
		fractionSumModulViw(idRow);
		//временные решения
		economicRowData.elements[idRow].SumParameters.modelType = economicRowData.elements[idRow].SumParameters.modelType != "currentyParameters" ? "currentyParameters" : "modelType";
		//Автоустановка дефолтных параметров валюты
		if (economicRowData.elements[idRow].SumParameters.currentyParameters.targetCurrent == "targetCurrent") {
			scrollBlockSumParam[0].getElementsByClassName('inputOption')[0].click();
		}
		refreshEconomicChart();
	});
	scrollBlockSumModelType[1].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
		fractionSumPerUnitModulView(idRow);
		//временные решения
		economicRowData.elements[idRow].SumParameters.modelType = economicRowData.elements[idRow].SumParameters.modelType != "fractionParameters" ? "fractionParameters" : "modelType";
		//Автоустановка дефолтных параметров валюты
		if (economicRowData.elements[idRow].SumParameters.currentyParameters.targetCurrent == "targetCurrent") {
			scrollBlockSumParam[0].getElementsByClassName('inputOption')[0].click();
		}
		//Автоустановка дефолтных параметров массы
		if (economicRowData.elements[idRow].SumParameters.fractionParameters.targetMassType == "targetMassType") {
			scrollBlockFractionMass[0].getElementsByClassName('inputOption')[0].click();
		}
		refreshEconomicChart();
	});
	scrollBlockSumModelType[2].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
		fractionSumPercentUnitModulView(idRow);
		//временные решения
		economicRowData.elements[idRow].SumParameters.modelType = economicRowData.elements[idRow].SumParameters.modelType != "fractionParametres" ? "fractionParametres" : "modelType";
		refreshEconomicChart();
	});
	//Учёт валют (временное решение)
	scrollBlockSumParam[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].SumParameters.currentyParameters.curentyValue.RUB = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockSumParam[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].SumParameters.currentyParameters.curentyValue.USD = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockSumParam[2].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].SumParameters.currentyParameters.curentyValue.EUR = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	//Учёт масс
	scrollBlockFractionMass[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].SumParameters.fractionParameters.massValue.ton = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockFractionMass[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].SumParameters.fractionParameters.massValue.cwt = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockFractionMass[2].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].SumParameters.fractionParameters.massValue.kg = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	for (var i = 0; i < scrollBlockSumModelType.length; i++) {
		var inputOption = scrollBlockSumModelType[i].getElementsByClassName('inputOption')[0];
		inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
	}
	for (var i = 0; i < scrollBlockSumParam.length; i++) {
		var inputOption = scrollBlockSumParam[i].getElementsByClassName('inputOption')[0];
		inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
		inputOption.addEventListener("click", setupTargetCurrenty(i, idRow));
	}
	for (var i = 0; i < scrollBlockFraction.length; i++) {
		var inputOption = scrollBlockFraction[i].getElementsByClassName('inputOption')[0];
		inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
		inputOption.addEventListener("click", setupTargetFraction(i, idRow));
	}
	for (var i = 0; i < scrollBlockFractionMass.length; i++) {
		var inputOption = scrollBlockFractionMass[i].getElementsByClassName('inputOption')[0];
		inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
		inputOption.addEventListener("click", setupMassType(i, idRow));
	}
	/*END SumParameters*/

	/*START DateParameters*/
	//блоки компонента
	var economDateModelType = row.children[0].children[2].children[1].children[1].children[0].children[0];
	var economDateParam = row.children[0].children[2].children[1].children[1].children[0].children[2];
	var economPeriodParam = row.children[0].children[2].children[1].children[1].children[0].children[4];
	var economFixedDate = row.children[0].children[2].children[1].children[1].children[0].children[6];

	//Скролл блоки
	var scrollBlockDateModelType = economDateModelType.children[0].children[0].children;
	var scrollBlockDateParam = economDateParam.children[0].children[0].children;
	var scrollBlockPeriodParam = economPeriodParam.children[0].children[0].children;
	var scrollBlockFixedDate = economFixedDate.children[0].children[0].children;
	var scrollBlockPeriodParam = economPeriodParam.children[0].children[0].children;
	//Добавление функций расскрывание модулей
	scrollBlockDateModelType[0].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
		fractionDateParamModulView(idRow);
		fractionPeriodParamModulView(idRow);
		//временное решение
		economicRowData.elements[idRow].DateParameters.modelType = economicRowData.elements[idRow].DateParameters.modelType != "calendarTime" ? "calendarTime" : "modelType";
		scrollBlockDateParam[3].getElementsByClassName('inputOption')[0].click();
	});
	scrollBlockDateModelType[1].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
		fractionDateParamModulView(idRow);
		fractionPeriodParamModulView(idRow);
		//временное решение
		economicRowData.elements[idRow].DateParameters.modelType = economicRowData.elements[idRow].DateParameters.modelType != "equipmentOperatingTime" ? "equipmentOperatingTime" : "modelType";
		scrollBlockDateParam[0].getElementsByClassName('inputOption')[0].click();
	});
	scrollBlockDateModelType[2].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
		fractionFixedDateModulView(idRow);
		//временное решение
		economicRowData.elements[idRow].DateParameters.modelType = economicRowData.elements[idRow].DateParameters.modelType != "fixedDate" ? "fixedDate" : "modelType";
	});

	//Учёт параметров времени
	scrollBlockDateParam[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.000" : this.value;
		economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.hour = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockDateParam[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.day = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockDateParam[2].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.week = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockDateParam[3].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.month = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	scrollBlockDateParam[4].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.year = Number(this.value).toFixed(1);
		this.value = Number(this.value).toFixed(1);
		refreshEconomicChart();
	});
	//Учёт параметров периода действия	
	scrollBlockPeriodParam[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].DateParameters.periodParametres.startPeriod = Number(this.value).toFixed(0);
		this.value = Number(this.value).toFixed(0);
		refreshEconomicChart();
	});
	scrollBlockPeriodParam[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
		this.value = Number(this.value) < 0 ? "0.00" : this.value;
		economicRowData.elements[idRow].DateParameters.periodParametres.endPeriod = Number(this.value).toFixed(0);
		this.value = Number(this.value).toFixed(0);
		refreshEconomicChart();
	});

	//Функции визуальной окраски
	for (var i = 0; i < scrollBlockDateModelType.length; i++) {
		var inputOption = scrollBlockDateModelType[i].getElementsByClassName('inputOption')[0];
		inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
	}
	for (var i = 0; i < scrollBlockDateParam.length; i++) {
		var inputOption = scrollBlockDateParam[i].getElementsByClassName('inputOption')[0];
		inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
		inputOption.addEventListener("click", setupTargetTime(i, idRow));
	}
	for (var i = 0; i < scrollBlockFixedDate.length; i++) {
		var inputOption = scrollBlockFixedDate[i].getElementsByClassName('inputOption')[0];
	}

	/*END DateParameters*/

	economicMainRow.appendChild(row);
	//создание данных под строку
	generateEconomicRowData();
	//запишем дефонлтные данные строки
	setupSumParametrText(idRow);	
}
function economicrefreshID(){
	var rows = document.getElementById('economicMainRow');
	for(var z = 1; z < rows.children.length; z++){
		var idRow = z;
		var cloneRow = clearEventListener(rows.children[z]);

		cloneRow.id = 'economicComponent_' + idRow;	
		cloneRow.children[0].children[0].id = 'economicRowNumber_' + idRow;
		cloneRow.children[0].children[0].addEventListener('mouseenter', economicShowDeleteButton('economicRowNumber_' + idRow));
		cloneRow.children[0].children[0].addEventListener('mouseleave', economicHideDeleteButton('economicRowNumber_' + idRow))
		cloneRow.children[0].children[0].children[0].id = 'economicComponentNumber_' + idRow;
		cloneRow.children[0].children[0].children[0].textContent = idRow;
		cloneRow.children[0].children[0].children[1].id = 'economicDeleteButton_' + idRow;
		cloneRow.children[0].children[0].children[1].addEventListener('click', economicRemoveRow('economicDeleteButton_' + idRow));
		cloneRow.children[0].children[0].children[1].addEventListener('click', refreshEconomicChart());
		// economicSumParametr 
		cloneRow.children[0].children[2].id = "economicSumParametr_" + idRow;
		cloneRow.children[0].children[2].children[1].children[0].children[0].id = 'economSumModelType_' + idRow;
		cloneRow.children[0].children[2].children[1].children[0].children[2].id = 'economSumParam_' + idRow;
		cloneRow.children[0].children[2].children[1].children[0].children[2].children[2].id = 'economFraction_' + idRow;
		cloneRow.children[0].children[2].children[1].children[0].children[2].children[3].id = 'economFractionMass_' + idRow;
		cloneRow.children[0].children[2].children[1].children[0].children[2].children[5].id = 'economPercentParam_' + idRow;
		cloneRow.children[0].children[2].children[1].children[0].children[2].children[5].children[1].id = 'economArticle_' + idRow;
		cloneRow.children[0].children[2].children[1].children[1].children[0].id = 'economicDateParameter_' + idRow;
		cloneRow.children[0].children[2].children[1].children[1].children[0].children[0].id = 'economDateModelType_' + idRow;
		cloneRow.children[0].children[2].children[1].children[1].children[0].children[2].id = 'economDateParam_' + idRow;
		cloneRow.children[0].children[2].children[1].children[1].children[0].children[4].id = 'economPeriodParam_' + idRow;
		cloneRow.children[0].children[2].children[1].children[1].children[0].children[6].id = 'economFixedDate_' + idRow;
		// row
		cloneRow.children[0].children[3].children[0].children[0].children[0].id = 'arrow_' + idRow;
		cloneRow.children[0].children[3].children[0].children[0].children[0].addEventListener("click", function () {
			economicRowData.elements[idRow].IncomeArrow = this.checked;
			refreshEconomicChart();
		});
		cloneRow.children[0].children[2].children[0].children[0].children[0].addEventListener("click", function () {
			fractionSumParametersView(idRow);
			setupSumParametrText(idRow);
			refreshEconomicChart();
		});
		cloneRow.children[0].children[2].children[0].children[1].children[0].addEventListener("click", function () {
			fractionSumParametersView(idRow);
			setupSumParametrText(idRow);
			refreshEconomicChart();
		});
		var economSumModelType = cloneRow.children[0].children[2].children[1].children[0].children[0];
		var economSumParam = cloneRow.children[0].children[2].children[1].children[0].children[2];
		var economFraction = cloneRow.children[0].children[2].children[1].children[0].children[2].children[2];
		var economFractionMass = cloneRow.children[0].children[2].children[1].children[0].children[2].children[3];
		var scrollBlockSumModelType = economSumModelType.children[0].children[0].children;
		var scrollBlockSumParam = economSumParam.children[0].children[0].children;
		var scrollBlockFraction = economFraction.children[0].children[0].children;
		var scrollBlockFractionMass = economFractionMass.children[0].children[0].children;

		scrollBlockSumModelType[0].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
			fractionSumModulViw(idRow);
			//временные решения
			economicRowData.elements[idRow].SumParameters.modelType = economicRowData.elements[idRow].SumParameters.modelType != "currentyParameters" ? "currentyParameters" : "modelType";
			//Автоустановка дефолтных параметров валюты
			if (economicRowData.elements[idRow].SumParameters.currentyParameters.targetCurrent == "targetCurrent") {
				scrollBlockSumParam[0].getElementsByClassName('inputOption')[0].click();
			}
			refreshEconomicChart();
		});
		scrollBlockSumModelType[1].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
			fractionSumPerUnitModulView(idRow);
			//временные решения
			economicRowData.elements[idRow].SumParameters.modelType = economicRowData.elements[idRow].SumParameters.modelType != "fractionParameters" ? "fractionParameters" : "modelType";
			//Автоустановка дефолтных параметров валюты
			if (economicRowData.elements[idRow].SumParameters.currentyParameters.targetCurrent == "targetCurrent") {
				scrollBlockSumParam[0].getElementsByClassName('inputOption')[0].click();
			}
			//Автоустановка дефолтных параметров массы
			if (economicRowData.elements[idRow].SumParameters.fractionParameters.targetMassType == "targetMassType") {
				scrollBlockFractionMass[0].getElementsByClassName('inputOption')[0].click();
			}
			refreshEconomicChart();
		});
		scrollBlockSumModelType[2].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
			fractionSumPercentUnitModulView(idRow);
			//временные решения
			economicRowData.elements[idRow].SumParameters.modelType = economicRowData.elements[idRow].SumParameters.modelType != "fractionParametres" ? "fractionParametres" : "modelType";
			refreshEconomicChart();
		});
		//Учёт валют (временное решение)
		scrollBlockSumParam[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].SumParameters.currentyParameters.curentyValue.RUB = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockSumParam[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].SumParameters.currentyParameters.curentyValue.USD = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockSumParam[2].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].SumParameters.currentyParameters.curentyValue.EUR = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		//Учёт масс
		scrollBlockFractionMass[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].SumParameters.fractionParameters.massValue.ton = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockFractionMass[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].SumParameters.fractionParameters.massValue.cwt = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockFractionMass[2].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].SumParameters.fractionParameters.massValue.kg = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		for (var i = 0; i < scrollBlockSumModelType.length; i++) {
			var inputOption = scrollBlockSumModelType[i].getElementsByClassName('inputOption')[0];
			inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
		}
		for (var i = 0; i < scrollBlockSumParam.length; i++) {
			var inputOption = scrollBlockSumParam[i].getElementsByClassName('inputOption')[0];
			inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
			inputOption.addEventListener("click", setupTargetCurrenty(i, idRow));
		}
		for (var i = 0; i < scrollBlockFraction.length; i++) {
			var inputOption = scrollBlockFraction[i].getElementsByClassName('inputOption')[0];
			inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
			inputOption.addEventListener("click", setupTargetFraction(i, idRow));
		}
		for (var i = 0; i < scrollBlockFractionMass.length; i++) {
			var inputOption = scrollBlockFractionMass[i].getElementsByClassName('inputOption')[0];
			inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
			inputOption.addEventListener("click", setupMassType(i, idRow));
		}
		/*END SumParameters*/

		/*START DateParameters*/
		//блоки компонента
		var economDateModelType = cloneRow.children[0].children[2].children[1].children[1].children[0].children[0];
		var economDateParam = cloneRow.children[0].children[2].children[1].children[1].children[0].children[2];
		var economPeriodParam = cloneRow.children[0].children[2].children[1].children[1].children[0].children[4];
		var economFixedDate = cloneRow.children[0].children[2].children[1].children[1].children[0].children[6];

		//Скролл блоки
		var scrollBlockDateModelType = economDateModelType.children[0].children[0].children;
		var scrollBlockDateParam = economDateParam.children[0].children[0].children;
		var scrollBlockPeriodParam = economPeriodParam.children[0].children[0].children;
		var scrollBlockFixedDate = economFixedDate.children[0].children[0].children;
		var scrollBlockPeriodParam = economPeriodParam.children[0].children[0].children;
		//Добавление функций расскрывание модулей
		scrollBlockDateModelType[0].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
			fractionDateParamModulView(idRow);
			fractionPeriodParamModulView(idRow);
			//временное решение
			economicRowData.elements[idRow].DateParameters.modelType = economicRowData.elements[idRow].DateParameters.modelType != "calendarTime" ? "calendarTime" : "modelType";
			scrollBlockDateParam[3].getElementsByClassName('inputOption')[0].click();
		});
		scrollBlockDateModelType[1].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
			fractionDateParamModulView(idRow);
			fractionPeriodParamModulView(idRow);
			//временное решение
			economicRowData.elements[idRow].DateParameters.modelType = economicRowData.elements[idRow].DateParameters.modelType != "equipmentOperatingTime" ? "equipmentOperatingTime" : "modelType";
			scrollBlockDateParam[0].getElementsByClassName('inputOption')[0].click();
		});
		scrollBlockDateModelType[2].getElementsByClassName('inputOption')[0].addEventListener('click', function () {
			fractionFixedDateModulView(idRow);
			//временное решение
			economicRowData.elements[idRow].DateParameters.modelType = economicRowData.elements[idRow].DateParameters.modelType != "fixedDate" ? "fixedDate" : "modelType";
		});

		//Учёт параметров времени
		scrollBlockDateParam[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.000" : this.value;
			economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.hour = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockDateParam[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.day = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockDateParam[2].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.week = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockDateParam[3].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.month = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		scrollBlockDateParam[4].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].DateParameters.timeParameters.timeValue.year = Number(this.value).toFixed(1);
			this.value = Number(this.value).toFixed(1);
			refreshEconomicChart();
		});
		//Учёт параметров периода действия	
		scrollBlockPeriodParam[0].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].DateParameters.periodParametres.startPeriod = Number(this.value).toFixed(0);
			this.value = Number(this.value).toFixed(0);
			refreshEconomicChart();
		});
		scrollBlockPeriodParam[1].getElementsByClassName('inputElement')[0].addEventListener('change', function () {
			this.value = Number(this.value) < 0 ? "0.00" : this.value;
			economicRowData.elements[idRow].DateParameters.periodParametres.endPeriod = Number(this.value).toFixed(0);
			this.value = Number(this.value).toFixed(0);
			refreshEconomicChart();
		});

		//Функции визуальной окраски
		for (var i = 0; i < scrollBlockDateModelType.length; i++) {
			var inputOption = scrollBlockDateModelType[i].getElementsByClassName('inputOption')[0];
			inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
		}
		for (var i = 0; i < scrollBlockDateParam.length; i++) {
			var inputOption = scrollBlockDateParam[i].getElementsByClassName('inputOption')[0];
			inputOption.addEventListener("click", setumMainElenetInBlock(inputOption));
			inputOption.addEventListener("click", setupTargetTime(i, idRow));
		}
		for (var i = 0; i < scrollBlockFixedDate.length; i++) {
			var inputOption = scrollBlockFixedDate[i].getElementsByClassName('inputOption')[0];
		}
	}
}