var Sustatment = {
	'ColumnState': ["active","lock","unlock"]
}

var requirementsTable = {
	"mainFractionData":{
		"purity": 0.000,
		"mass": 1.000,
		"percent_exit": 100.00
	},
	"suitableFraction":{
		"purity": 0.000,
		"mass": 1.000,
		"percent_exit": 100.00
	},
	"weedFraction":{
		"purity": 0.000,
		"mass": 0.000,
		"percent_exit": 0.00
	}	
	/*
	//Пригодиться для большего числа фракций
	"otherFraction": [],
	*/
}
var componentRow = [];

function setupComponentRow(){
	componentRow.push({
		"component_name": "component_name",
		"mainFractionData":{
			"calcToggle": true,
			"impToggle": false,
			"acceptRejectToggle": true,
			"unitOption":{
				"percent": componentRow.length == 0 ? 100.0 : 0.00,
				"gram": 0.0,
				"pieces": 0.0,
				"pieces_kg": 0.0,
				"ppm": 0.0
			},
			"hingeMass": componentRow[0] != null ? componentRow[0].mainFractionData.hingeMass : 100.00,
			"pieces_1000": 100.00
		},
		"suitableFractionData":{
			"calcToggle": true,
			"impToggle": false,
			"acceptRejectToggle": true,
			"unitOption":{
				"percent": componentRow.length == 0 ? 100.0 : 0.00,
				"gram": 0.0,
				"pieces": 0.0,
				"pieces_kg": 0.0,
				"ppm	": 0.0
				//"iterfraction_percent": 0.0
			},
			"hingeMass": componentRow[0] != null ? componentRow[0].suitableFractionData.hingeMass : 100.00,
			"pieces_1000": 100.000
		},
		"weedFractionData":{
			"calcToggle": true,
			"impToggle": false,
			"acceptRejectToggle": true,
			"unitOption":{
				"percent": componentRow.length == 1 ? 100.0 : 0.00,
				"gram": 0.0,
				"pieces": 0.0,
				"pieces_kg": 0.0,
				"ppm": 0.0
				//"iterfraction_percent": 0.0
			},
			"hingeMass": componentRow[0] != null ? componentRow[0].weedFractionData.hingeMass : 100.00,
			"pieces_1000": 100.00
		}		
	});
}

//функции компонентов
function setupComponentName(){
	var idRow = this.id.split("_")[1];
	var mainRow = "mainRow_" + idRow;
	var inputFilter = document.getElementById(mainRow).getElementsByClassName("inputFilter")[0]
	
	componentRow[idRow-1].component_name = inputFilter.value != "" ? inputFilter.value : inputFilter.placeholder;
}
function setupComponentToggles(toggle){
	var idRow = toggle.parentNode.parentNode.parentNode.id.split("_")[2];
	var idFraction = toggle.parentNode.parentNode.parentNode.id.split("_")[1];
	var imgName = toggle.style.backgroundImage.split('/')[5].split('.')[0];
	
	//Определение фракции
	switch(idFraction){
		case "1":
			var fractionData = componentRow[idRow-1].mainFractionData;
			break;
		case "2":
			var fractionData = componentRow[idRow-1].suitableFractionData;
			break;
		case "3":
			var fractionData = componentRow[idRow-1].weedFractionData;
			break;
	}
	//Отпределение тогла
	switch(imgName){
		case "calcOn":
			fractionData.calcToggle = true;
			break;
		case "calcOff":
			fractionData.calcToggle = false;
			break;
		case "impOn":
			fractionData.impToggle = true;
			break;
		case "impOff":
			fractionData.impToggle = false;
			break;
		case "accept":
			fractionData.acceptRejectToggle = true;
			break;
		case "reject":
			fractionData.acceptRejectToggle = false;
			break;
	}
	requirementsPurityUpdate();
}
//Функции компоментов фракций
function mathfComponentFunction(element_id){
	var element = document.getElementById(element_id);
	var sliderBlock = element.children[0];
	var hingeMassBlock = element.children[2];
	var piecesBlock = element.children[4];
	
	var idRow = element.id.split("_")[2];
	var idFraction = element.id.split("_")[1];
	
	//Определение фракции
	switch(idFraction){
		case "1":
			var fractionData = componentRow[idRow-1].mainFractionData;
			break;
		case "2":
			var fractionData = componentRow[idRow-1].suitableFractionData;
			break;
		case "3":
			var fractionData = componentRow[idRow-1].weedFractionData;
			break;
	}
	
	hingeMassBlock.children[0].children[0].value = fractionData.hingeMass;
	
	sliderBlock.children[0].children[0].addEventListener("change", componentPercentUpdate(idFraction));
	sliderBlock.children[1].children[0].addEventListener("change", componentGramUpdate(idFraction));
	sliderBlock.children[2].children[0].addEventListener("change", componentPiecesUpdate(idFraction));
	sliderBlock.children[3].children[0].addEventListener("change", componentPiecesKgUpdate(idFraction));
	sliderBlock.children[4].children[0].addEventListener("change", componentPPM_Update(idFraction));
	
	hingeMassBlock.children[0].children[0].addEventListener("change", componentPercentUpdate(idFraction));
	piecesBlock.children[0].children[0].addEventListener("change", componentPercentUpdate(idFraction));
	
	sliderBlock.children[0].children[0].addEventListener("change", updateRemovedPercent);
	sliderBlock.children[1].children[0].addEventListener("change", updateRemovedPercent);
	sliderBlock.children[2].children[0].addEventListener("change", updateRemovedPercent);
	sliderBlock.children[3].children[0].addEventListener("change", updateRemovedPercent);
	sliderBlock.children[4].children[0].addEventListener("change", updateRemovedPercent);
	
	hingeMassBlock.children[0].children[0].addEventListener("change", updateRemovedPercent);
	piecesBlock.children[0].children[0].addEventListener("change", updateRemovedPercent);
	
	
}
function sumComponentPercent(idFraction){
	var sumComponent = 0;
	for(var i = 0; i < componentRow.length; i++){
		switch(idFraction){
			case "1":
				sumComponent += Number(componentRow[i].mainFractionData.unitOption.percent);
				break;
			case "2":
				sumComponent += Number(componentRow[i].suitableFractionData.unitOption.percent);
				break;
			case "3":
				sumComponent += Number(componentRow[i].weedFractionData.unitOption.percent);
				break;
		}
	}
	return sumComponent;
}
function sumComponentPieces_KG(idFraction){
	var sumComponent = 0;
	for(var i = 0; i < componentRow.length; i++){
		switch(idFraction){
			case "1":
				sumComponent += Number(componentRow[i].mainFractionData.unitOption.pieces_kg);
				break;
			case "2":
				sumComponent += Number(componentRow[i].suitableFractionData.unitOption.pieces_kg);
				break;
			case "3":
				sumComponent += Number(componentRow[i].weedFractionData.unitOption.pieces_kg);
				break;
		}
	}
	return sumComponent;
}

//Обновление значениий процентовок
function componentPercentUpdate(idFraction){
	return function e(){
		var DropdownBlock = this.parentNode.parentNode.parentNode;
		var MainScrollBlock = DropdownBlock.children[0];
		var HingeMass = DropdownBlock.children[2].children[0].children[0];
		var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];
		
		//Основные параметры
		var percent = MainScrollBlock.children[0].children[0];
		var gram = MainScrollBlock.children[1].children[0];
		var pieces = MainScrollBlock.children[2].children[0];
		var pieces_kg = MainScrollBlock.children[3].children[0];
		var ppm = MainScrollBlock.children[4].children[0];
		
		var idRow = DropdownBlock.id.split("_")[2];
		
		switch(idFraction){
			case "1":
				var firstElement = componentRow[0].mainFractionData.unitOption;
				var targetElement = componentRow[idRow-1].mainFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].mainFractionData.unitOption;
				break;
			case "2":
				var firstElement = componentRow[0].suitableFractionData.unitOption;
				var targetElement = componentRow[idRow-1].suitableFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].suitableFractionData.unitOption;
				break;
			case "3":
				var firstElement = componentRow[0].weedFractionData.unitOption;
				var targetElement = componentRow[idRow-1].weedFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].weedFractionData.unitOption;
				break;
		}
		
		//Основное значение
		if(idRow == 1){
			targetElement.percent = percent.value <= Number(targetElement.percent) + Number(lastElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(targetElement.percent) + Number(lastElement.percent)).toFixed(2)
			lastElement.percent = lastElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		else{
			targetElement.percent = percent.value <= Number(firstElement.percent) + Number(targetElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(firstElement.percent) + Number(targetElement.percent)).toFixed(2)
			firstElement.percent = firstElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		
		for(var i = 1; i <= componentRow.length; i++){
			var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
			var MainScrollBlock = DropdownBlock.children[0];
			var HingeMass = DropdownBlock.children[2].children[0].children[0];
			var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

			//Основные параметры
			var percent = MainScrollBlock.children[0].children[0];
			var gram = MainScrollBlock.children[1].children[0];
			var pieces = MainScrollBlock.children[2].children[0];
			var pieces_kg = MainScrollBlock.children[3].children[0];
			var ppm = MainScrollBlock.children[4].children[0];
			
			//Основное значение
			switch(idFraction){
				case "1":
					percent.value = Number(componentRow[i-1].mainFractionData.unitOption.percent).toFixed(2);
					break;
				case "2":
					percent.value =  Number(componentRow[i-1].suitableFractionData.unitOption.percent).toFixed(2);
					break;
				case "3":
					percent.value =  Number(componentRow[i-1].weedFractionData.unitOption.percent).toFixed(2);
					break;
			}
			
			//Остальные значения
			gram.value = Number(HingeMass.value / 100 * percent.value).toFixed(2);
			pieces.value = Number(gram.value / (Pieces_1000.value / 1000)).toFixed(2);
			pieces_kg.value =  Number((percent.value * 10) / (Pieces_1000.value / 1000)).toFixed(2);
			//Значение компонента
			switch(idFraction){
				case "1":
					//Значение компонента
					componentRow[i-1].mainFractionData.unitOption.percent = percent.value;
					componentRow[i-1].mainFractionData.unitOption.gram = gram.value;
					componentRow[i-1].mainFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].mainFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].mainFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].mainFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "2":
					componentRow[i-1].suitableFractionData.unitOption.percent = percent.value;
					componentRow[i-1].suitableFractionData.unitOption.gram = gram.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].suitableFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].suitableFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "3":
					componentRow[i-1].weedFractionData.unitOption.percent = percent.value;
					componentRow[i-1].weedFractionData.unitOption.gram = gram.value;
					componentRow[i-1].weedFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].weedFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].weedFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].weedFractionData.pieces_1000 = Pieces_1000.value;
					break;
			}
			
			DropdownBlock.parentNode.parentNode.children[0].children[0].children[0].value = percent.value;
			DropdownBlock.parentNode.parentNode.children[1].children[0].value = percent.value + " %";
		}
		requirementsPurityUpdate();
		updatePPM_Components(idFraction);
	}
}

//Обновление значениий граммовок
function componentGramUpdate(idFraction){
	return function e(){
		var DropdownBlock = this.parentNode.parentNode.parentNode;
		var MainScrollBlock = DropdownBlock.children[0];
		var HingeMass = DropdownBlock.children[2].children[0].children[0];
		var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];
		
		//Основные параметры
		var percent = MainScrollBlock.children[0].children[0];
		var gram = MainScrollBlock.children[1].children[0];
		var pieces = MainScrollBlock.children[2].children[0];
		var pieces_kg = MainScrollBlock.children[3].children[0];
		var ppm = MainScrollBlock.children[4].children[0];
		
		var idRow = DropdownBlock.id.split("_")[2];
		
		percent.value = Number(gram.value / HingeMass.value * 100).toFixed(2);
		
		switch(idFraction){
			case "1":
				var firstElement = componentRow[0].mainFractionData.unitOption;
				var targetElement = componentRow[idRow-1].mainFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].mainFractionData.unitOption;
				break;
			case "2":
				var firstElement = componentRow[0].suitableFractionData.unitOption;
				var targetElement = componentRow[idRow-1].suitableFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].suitableFractionData.unitOption;
				break;
			case "3":
				var firstElement = componentRow[0].weedFractionData.unitOption;
				var targetElement = componentRow[idRow-1].weedFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].weedFractionData.unitOption;
				break;
		}

		//Основное значение
		if(idRow == 1){
			targetElement.percent = percent.value <= Number(targetElement.percent) + Number(lastElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(targetElement.percent) + Number(lastElement.percent)).toFixed(2)
			lastElement.percent = lastElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		else{
			targetElement.percent = percent.value <= Number(firstElement.percent) + Number(targetElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(firstElement.percent) + Number(targetElement.percent)).toFixed(2)
			firstElement.percent = firstElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		
		for(var i = 1; i <= componentRow.length; i++){
			var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
			var MainScrollBlock = DropdownBlock.children[0];
			var HingeMass = DropdownBlock.children[2].children[0].children[0];
			var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

			//Основные параметры
			var percent = MainScrollBlock.children[0].children[0];
			var gram = MainScrollBlock.children[1].children[0];
			var pieces = MainScrollBlock.children[2].children[0];
			var pieces_kg = MainScrollBlock.children[3].children[0];
			var ppm = MainScrollBlock.children[4].children[0];
			
			//Основное значение
			switch(idFraction){
				case "1":
					percent.value = Number(componentRow[i-1].mainFractionData.unitOption.percent).toFixed(2);
					break;
				case "2":
					percent.value =  Number(componentRow[i-1].suitableFractionData.unitOption.percent).toFixed(2);
					break;
				case "3":
					percent.value =  Number(componentRow[i-1].weedFractionData.unitOption.percent).toFixed(2);
					break;
			}

			//Остальные значения
			gram.value = Number(HingeMass.value / 100 * percent.value).toFixed(2);
			pieces.value = Number(gram.value / (Pieces_1000.value / 1000)).toFixed(2);
			pieces_kg.value =  Number((percent.value * 10) / (Pieces_1000.value / 1000)).toFixed(2);
			//Значение компонента
			switch(idFraction){
				case "1":
					//Значение компонента
					componentRow[i-1].mainFractionData.unitOption.percent = percent.value;
					componentRow[i-1].mainFractionData.unitOption.gram = gram.value;
					componentRow[i-1].mainFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].mainFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].mainFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].mainFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "2":
					componentRow[i-1].suitableFractionData.unitOption.percent = percent.value;
					componentRow[i-1].suitableFractionData.unitOption.gram = gram.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].suitableFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].suitableFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "3":
					componentRow[i-1].weedFractionData.unitOption.percent = percent.value;
					componentRow[i-1].weedFractionData.unitOption.gram = gram.value;
					componentRow[i-1].weedFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].weedFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].weedFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].weedFractionData.pieces_1000 = Pieces_1000.value;
					break;
			}
			DropdownBlock.parentNode.parentNode.children[0].children[0].children[0].value = percent.value;
			DropdownBlock.parentNode.parentNode.children[1].children[0].value = percent.value + " %"
		}
		requirementsPurityUpdate();
		updatePPM_Components(idFraction);
	}
}

function componentPiecesUpdate(idFraction){
	return function e(){
		var DropdownBlock = this.parentNode.parentNode.parentNode;
		var MainScrollBlock = DropdownBlock.children[0];
		var HingeMass = DropdownBlock.children[2].children[0].children[0];
		var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];
		
		//Основные параметры
		var percent = MainScrollBlock.children[0].children[0];
		var gram = MainScrollBlock.children[1].children[0];
		var pieces = MainScrollBlock.children[2].children[0];
		var pieces_kg = MainScrollBlock.children[3].children[0];
		var ppm = MainScrollBlock.children[4].children[0];
		
		var idRow = DropdownBlock.id.split("_")[2];
		
		gram.value = Number(pieces.value * (Pieces_1000.value / 1000)).toFixed(2);
		percent.value = Number(gram.value / HingeMass.value * 100).toFixed(2);
		
		switch(idFraction){
			case "1":
				var firstElement = componentRow[0].mainFractionData.unitOption;
				var targetElement = componentRow[idRow-1].mainFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].mainFractionData.unitOption;
				break;
			case "2":
				var firstElement = componentRow[0].suitableFractionData.unitOption;
				var targetElement = componentRow[idRow-1].suitableFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].suitableFractionData.unitOption;
				break;
			case "3":
				var firstElement = componentRow[0].weedFractionData.unitOption;
				var targetElement = componentRow[idRow-1].weedFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].weedFractionData.unitOption;
				break;
		}

		//Основное значение
		if(idRow == 1){
			targetElement.percent = percent.value <= Number(targetElement.percent) + Number(lastElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(targetElement.percent) + Number(lastElement.percent)).toFixed(2)
			lastElement.percent = lastElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		else{
			targetElement.percent = percent.value <= Number(firstElement.percent) + Number(targetElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(firstElement.percent) + Number(targetElement.percent)).toFixed(2)
			firstElement.percent = firstElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		
		for(var i = 1; i <= componentRow.length; i++){
			var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
			var MainScrollBlock = DropdownBlock.children[0];
			var HingeMass = DropdownBlock.children[2].children[0].children[0];
			var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

			//Основные параметры
			var percent = MainScrollBlock.children[0].children[0];
			var gram = MainScrollBlock.children[1].children[0];
			var pieces = MainScrollBlock.children[2].children[0];
			var pieces_kg = MainScrollBlock.children[3].children[0];
			var ppm = MainScrollBlock.children[4].children[0];
			
			//Основное значение
			switch(idFraction){
				case "1":
					percent.value = Number(componentRow[i-1].mainFractionData.unitOption.percent).toFixed(2);
					break;
				case "2":
					percent.value =  Number(componentRow[i-1].suitableFractionData.unitOption.percent).toFixed(2);
					break;
				case "3":
					percent.value =  Number(componentRow[i-1].weedFractionData.unitOption.percent).toFixed(2);
					break;
			}

			//Остальные значения
			gram.value = Number(HingeMass.value / 100 * percent.value).toFixed(2);
			pieces.value = Number(gram.value / (Pieces_1000.value / 1000)).toFixed(2);
			pieces_kg.value =  Number((percent.value * 10) / (Pieces_1000.value / 1000)).toFixed(2);
			//Значение компонента
			switch(idFraction){
				case "1":
					//Значение компонента
					componentRow[i-1].mainFractionData.unitOption.percent = percent.value;
					componentRow[i-1].mainFractionData.unitOption.gram = gram.value;
					componentRow[i-1].mainFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].mainFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].mainFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].mainFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "2":
					componentRow[i-1].suitableFractionData.unitOption.percent = percent.value;
					componentRow[i-1].suitableFractionData.unitOption.gram = gram.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].suitableFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].suitableFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "3":
					componentRow[i-1].weedFractionData.unitOption.percent = percent.value;
					componentRow[i-1].weedFractionData.unitOption.gram = gram.value;
					componentRow[i-1].weedFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].weedFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].weedFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].weedFractionData.pieces_1000 = Pieces_1000.value;
					break;
			}
			DropdownBlock.parentNode.parentNode.children[0].children[0].children[0].value = percent.value;
			DropdownBlock.parentNode.parentNode.children[1].children[0].value = percent.value + " %"
		}
		requirementsPurityUpdate();
		updatePPM_Components(idFraction);
	}
}
//Обновление значениий штук/кг
function componentPiecesKgUpdate(idFraction){
	return function e(){
		var DropdownBlock = this.parentNode.parentNode.parentNode;
		var MainScrollBlock = DropdownBlock.children[0];
		var HingeMass = DropdownBlock.children[2].children[0].children[0];
		var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];
		
		//Основные параметры
		var percent = MainScrollBlock.children[0].children[0];
		var gram = MainScrollBlock.children[1].children[0];
		var pieces = MainScrollBlock.children[2].children[0];
		var pieces_kg = MainScrollBlock.children[3].children[0];
		var ppm = MainScrollBlock.children[4].children[0];
		
		var idRow = DropdownBlock.id.split("_")[2];
		
		percent.value = Number((pieces_kg.value / 10) * (Pieces_1000.value / 1000)).toFixed(2);
		
		switch(idFraction){
			case "1":
				var firstElement = componentRow[0].mainFractionData.unitOption;
				var targetElement = componentRow[idRow-1].mainFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].mainFractionData.unitOption;
				break;
			case "2":
				var firstElement = componentRow[0].suitableFractionData.unitOption;
				var targetElement = componentRow[idRow-1].suitableFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].suitableFractionData.unitOption;
				break;
			case "3":
				var firstElement = componentRow[0].weedFractionData.unitOption;
				var targetElement = componentRow[idRow-1].weedFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].weedFractionData.unitOption;
				break;
		}

		//Основное значение
		if(idRow == 1){
			targetElement.percent = percent.value <= Number(targetElement.percent) + Number(lastElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(targetElement.percent) + Number(lastElement.percent)).toFixed(2)
			lastElement.percent = lastElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		else{
			targetElement.percent = percent.value <= Number(firstElement.percent) + Number(targetElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(firstElement.percent) + Number(targetElement.percent)).toFixed(2)
			firstElement.percent = firstElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		
		for(var i = 1; i <= componentRow.length; i++){
			var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
			var MainScrollBlock = DropdownBlock.children[0];
			var HingeMass = DropdownBlock.children[2].children[0].children[0];
			var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

			//Основные параметры
			var percent = MainScrollBlock.children[0].children[0];
			var gram = MainScrollBlock.children[1].children[0];
			var pieces = MainScrollBlock.children[2].children[0];
			var pieces_kg = MainScrollBlock.children[3].children[0];
			var ppm = MainScrollBlock.children[4].children[0];
			
			//Основное значение
			switch(idFraction){
				case "1":
					percent.value = Number(componentRow[i-1].mainFractionData.unitOption.percent).toFixed(2);
					break;
				case "2":
					percent.value =  Number(componentRow[i-1].suitableFractionData.unitOption.percent).toFixed(2);
					break;
				case "3":
					percent.value =  Number(componentRow[i-1].weedFractionData.unitOption.percent).toFixed(2);
					break;
			}

			//Остальные значения
			gram.value = Number(HingeMass.value / 100 * percent.value).toFixed(2);
			pieces.value = Number(gram.value / (Pieces_1000.value / 1000)).toFixed(2);
			pieces_kg.value =  Number((percent.value * 10) / (Pieces_1000.value / 1000)).toFixed(2);
			ppm.value = Number(1000000 / sumComponentPieces_KG(idFraction) * pieces_kg.value);
			//Значение компонента
			switch(idFraction){
				case "1":
					//Значение компонента
					componentRow[i-1].mainFractionData.unitOption.percent = percent.value;
					componentRow[i-1].mainFractionData.unitOption.gram = gram.value;
					componentRow[i-1].mainFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].mainFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].mainFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].mainFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "2":
					componentRow[i-1].suitableFractionData.unitOption.percent = percent.value;
					componentRow[i-1].suitableFractionData.unitOption.gram = gram.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].suitableFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].suitableFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "3":
					componentRow[i-1].weedFractionData.unitOption.percent = percent.value;
					componentRow[i-1].weedFractionData.unitOption.gram = gram.value;
					componentRow[i-1].weedFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].weedFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].weedFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].weedFractionData.pieces_1000 = Pieces_1000.value;
					break;
			}
			DropdownBlock.parentNode.parentNode.children[0].children[0].children[0].value = percent.value;
			DropdownBlock.parentNode.parentNode.children[1].children[0].value = percent.value + " %"
		}
		requirementsPurityUpdate();
		updatePPM_Components(idFraction);
	}
}
//Обновление значениий промилий
function componentPPM_Update(idFraction){
	return function e(){
		var DropdownBlock = this.parentNode.parentNode.parentNode;
		var MainScrollBlock = DropdownBlock.children[0];
		var HingeMass = DropdownBlock.children[2].children[0].children[0];
		var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];
		
		//Основные параметры
		var percent = MainScrollBlock.children[0].children[0];
		var gram = MainScrollBlock.children[1].children[0];
		var pieces = MainScrollBlock.children[2].children[0];
		var pieces_kg = MainScrollBlock.children[3].children[0];
		var ppm = MainScrollBlock.children[4].children[0];
		
		var idRow = DropdownBlock.id.split("_")[2];
		
		pieces_kg.value = Number(ppm.value / (1000000 / sumComponentPieces_KG(idFraction))).toFixed(2);
		percent.value = Number((pieces_kg.value / 10) * (Pieces_1000.value / 1000)).toFixed(2);
		
		switch(idFraction){
			case "1":
				var firstElement = componentRow[0].mainFractionData.unitOption;
				var targetElement = componentRow[idRow-1].mainFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].mainFractionData.unitOption;
				break;
			case "2":
				var firstElement = componentRow[0].suitableFractionData.unitOption;
				var targetElement = componentRow[idRow-1].suitableFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].suitableFractionData.unitOption;
				break;
			case "3":
				var firstElement = componentRow[0].weedFractionData.unitOption;
				var targetElement = componentRow[idRow-1].weedFractionData.unitOption;
				var lastElement = componentRow[componentRow.length-1].weedFractionData.unitOption;
				break;
		}

		//Основное значение
		if(idRow == 1){
			targetElement.percent = percent.value <= Number(targetElement.percent) + Number(lastElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(targetElement.percent) + Number(lastElement.percent)).toFixed(2)
			lastElement.percent = lastElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		else{
			targetElement.percent = percent.value <= Number(firstElement.percent) + Number(targetElement.percent) ? Number(percent.value).toFixed(2) : Number(Number(firstElement.percent) + Number(targetElement.percent)).toFixed(2)
			firstElement.percent = firstElement.percent - (sumComponentPercent(idFraction) - 100);
		}
		
		for(var i = 1; i <= componentRow.length; i++){
			var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
			var MainScrollBlock = DropdownBlock.children[0];
			var HingeMass = DropdownBlock.children[2].children[0].children[0];
			var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

			//Основные параметры
			var percent = MainScrollBlock.children[0].children[0];
			var gram = MainScrollBlock.children[1].children[0];
			var pieces = MainScrollBlock.children[2].children[0];
			var pieces_kg = MainScrollBlock.children[3].children[0];
			var ppm = MainScrollBlock.children[4].children[0];
			
			//Основное значение
			switch(idFraction){
				case "1":
					percent.value = Number(componentRow[i-1].mainFractionData.unitOption.percent).toFixed(2);
					break;
				case "2":
					percent.value =  Number(componentRow[i-1].suitableFractionData.unitOption.percent).toFixed(2);
					break;
				case "3":
					percent.value =  Number(componentRow[i-1].weedFractionData.unitOption.percent).toFixed(2);
					break;
			}
			

			//Остальные значения
			gram.value = Number(HingeMass.value / 100 * percent.value).toFixed(2);
			pieces.value = Number(gram.value / (Pieces_1000.value / 1000)).toFixed(2);
			pieces_kg.value =  Number((percent.value * 10) / (Pieces_1000.value / 1000)).toFixed(2);
			//Значение компонента
			switch(idFraction){
				case "1":
					//Значение компонента
					componentRow[i-1].mainFractionData.unitOption.percent = percent.value;
					componentRow[i-1].mainFractionData.unitOption.gram = gram.value;
					componentRow[i-1].mainFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].mainFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].mainFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].mainFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "2":
					componentRow[i-1].suitableFractionData.unitOption.percent = percent.value;
					componentRow[i-1].suitableFractionData.unitOption.gram = gram.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].suitableFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].suitableFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].suitableFractionData.pieces_1000 = Pieces_1000.value;
					break;
				case "3":
					componentRow[i-1].weedFractionData.unitOption.percent = percent.value;
					componentRow[i-1].weedFractionData.unitOption.gram = gram.value;
					componentRow[i-1].weedFractionData.unitOption.pieces = pieces.value;
					componentRow[i-1].weedFractionData.unitOption.pieces_kg = pieces_kg.value;
					
					componentRow[i-1].weedFractionData.hingeMass = HingeMass.value;
					componentRow[i-1].weedFractionData.pieces_1000 = Pieces_1000.value;
					break;
			}
			DropdownBlock.parentNode.parentNode.children[0].children[0].children[0].value = percent.value;
			DropdownBlock.parentNode.parentNode.children[1].children[0].value = percent.value + " %"
		}
		requirementsPurityUpdate();
		updatePPM_Components(idFraction);
	}
}
//Обновление значениий процентовок при удалении-добавлении компонента
function updateRemovedPercent(){
	if(componentRow.length){
		componentRow[0].mainFractionData.unitOption.percent = componentRow[0].mainFractionData.unitOption.percent - (sumComponentPercent("1") - 100);
		componentRow[0].suitableFractionData.unitOption.percent = componentRow[0].suitableFractionData.unitOption.percent - (sumComponentPercent("2") - 100);
		componentRow[0].weedFractionData.unitOption.percent = componentRow[0].weedFractionData.unitOption.percent - (sumComponentPercent("3") - 100);
		
		for(var idFraction = 1; idFraction <= 3; idFraction++){ 
			for(var i = 1; i <= componentRow.length; i++){
				var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
				var MainScrollBlock = DropdownBlock.children[0];
				var HingeMass = DropdownBlock.children[2].children[0].children[0];
				var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

				//Основные параметры
				var percent = MainScrollBlock.children[0].children[0];
				var gram = MainScrollBlock.children[1].children[0];
				var pieces = MainScrollBlock.children[2].children[0];
				var pieces_kg = MainScrollBlock.children[3].children[0];
				var ppm = MainScrollBlock.children[4].children[0];
				
				//Основное значение
				switch(String(idFraction)){
					case "1":
						percent.value = Number(componentRow[i-1].mainFractionData.unitOption.percent).toFixed(2);
						break;
					case "2":
						percent.value =  Number(componentRow[i-1].suitableFractionData.unitOption.percent).toFixed(2);
						break;
					case "3":
						percent.value =  Number(componentRow[i-1].weedFractionData.unitOption.percent).toFixed(2);
						break;
				}

				//Остальные значения
				gram.value = Number(HingeMass.value / 100 * percent.value).toFixed(2);
				pieces.value = Number(gram.value / (Pieces_1000.value / 1000)).toFixed(2);
				pieces_kg.value =  Number((percent.value * 10) / (Pieces_1000.value / 1000)).toFixed(2);
				
				//Значение компонента
				switch(String(idFraction)){
					case "1":
						//Значение компонента
						componentRow[i-1].mainFractionData.unitOption.percent = percent.value;
						componentRow[i-1].mainFractionData.unitOption.gram = gram.value;
						componentRow[i-1].mainFractionData.unitOption.pieces = pieces.value;
						componentRow[i-1].mainFractionData.unitOption.pieces_kg = pieces_kg.value;
						componentRow[i-1].mainFractionData.unitOption.ppm = ppm.value;
						
						componentRow[i-1].mainFractionData.hingeMass = HingeMass.value;
						componentRow[i-1].mainFractionData.pieces_1000 = Pieces_1000.value;
						break;
					case "2":
						componentRow[i-1].suitableFractionData.unitOption.percent = percent.value;
						componentRow[i-1].suitableFractionData.unitOption.gram = gram.value;
						componentRow[i-1].suitableFractionData.unitOption.pieces = pieces.value;
						componentRow[i-1].suitableFractionData.unitOption.pieces_kg = pieces_kg.value;
						
						componentRow[i-1].suitableFractionData.hingeMass = HingeMass.value;
						componentRow[i-1].suitableFractionData.pieces_1000 = Pieces_1000.value;
						break;
					case "3":
						componentRow[i-1].weedFractionData.unitOption.percent = percent.value;
						componentRow[i-1].weedFractionData.unitOption.gram = gram.value;
						componentRow[i-1].weedFractionData.unitOption.pieces = pieces.value;
						componentRow[i-1].weedFractionData.unitOption.pieces_kg = pieces_kg.value;
						
						componentRow[i-1].weedFractionData.hingeMass = HingeMass.value;
						componentRow[i-1].weedFractionData.pieces_1000 = Pieces_1000.value;
						break;
				}
				DropdownBlock.parentNode.parentNode.children[0].children[0].children[0].value = percent.value;
				DropdownBlock.parentNode.parentNode.children[1].children[0].value = percent.value + " %"
			}
			updatePPM_Components(String(idFraction));
		}
		requirementsPurityUpdate();
	}	
}
function updatePPM_Components(idFraction){
	for(var i = 1; i <= componentRow.length; i++){
		var DropdownBlock = document.getElementById("massDropdown_"+idFraction+"_"+i);
		var MainScrollBlock = DropdownBlock.children[0];
		var HingeMass = DropdownBlock.children[2].children[0].children[0];
		var Pieces_1000	= DropdownBlock.children[4].children[0].children[0];

		//Основные параметры
		var percent = MainScrollBlock.children[0].children[0];
		var gram = MainScrollBlock.children[1].children[0];
		var pieces = MainScrollBlock.children[2].children[0];
		var pieces_kg = MainScrollBlock.children[3].children[0];
		var ppm = MainScrollBlock.children[4].children[0]

		ppm.value = Number(1000000 / sumComponentPieces_KG(idFraction) * pieces_kg.value).toFixed(2);
		
		switch(idFraction){
			case "1":
				componentRow[i-1].mainFractionData.unitOption.ppm = ppm.value;
				break;
			case "2":
				componentRow[i-1].suitableFractionData.unitOption.ppm = ppm.value;
				break;
			case "3":
				componentRow[i-1].weedFractionData.unitOption.ppm = ppm.value;
				break;
		}
	}
	requirementsPercentUpdate();
	updateData();
}

//функциии требований фракции 
function setupRequirementsTable(){
	//Айдишники на странице выделенны явно
	pureInpStart.value = Number(requirementsTable.mainFractionData.purity).toFixed(3);
	outputStart.value = Number(requirementsTable.mainFractionData.mass).toFixed(3);
	percentStart.value = Number(requirementsTable.mainFractionData.percent_exit).toFixed(2);
	
	pureInpGood.value = Number(requirementsTable.suitableFraction.purity).toFixed(3);
	outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
	percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
	
	pureInpTrash.value = Number(requirementsTable.weedFraction.purity).toFixed(3);
	outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
	percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
	
	//Привязка функций
	outputStart.addEventListener("change",requirementsMassUpdate);
	outputGood.addEventListener("change",requirementsMassUpdate);
	outputTrash.addEventListener("change",requirementsMassUpdate);
	
	percentGood.addEventListener("change",requirementsPercentUpdate);
	percentTrash.addEventListener("change",requirementsPercentUpdate);
	
	outputStart.addEventListener("change",updateRemovedPercent);
	outputGood.addEventListener("change",updateRemovedPercent);
	outputTrash.addEventListener("change",updateRemovedPercent);
	
	percentGood.addEventListener("change",updateRemovedPercent);
	percentTrash.addEventListener("change",updateRemovedPercent);
	
	outputStart.addEventListener("change",updateData);
	outputGood.addEventListener("change",updateData);
	outputTrash.addEventListener("change",updateData);
	
	percentGood.addEventListener("change",updateData);
	percentTrash.addEventListener("change",updateData);
	
	//Дефолтное обновление масс
	requirementsMassUpdate();

	//Вызов привязки слушателей для страницы экономического обоснования economic_model.js	
	setupOperationGraph();
}

function requirementsPurityUpdate(){
	var purityMainFraction = 0;
	var puritySuitableFraction = 0;
	var purityWeedFraction = 0;
	
	for(var i = 0; i < componentRow.length; i++){
		purityMainFraction += componentRow[i].mainFractionData.acceptRejectToggle ? Number(componentRow[i].mainFractionData.unitOption.percent) : 0;
		puritySuitableFraction += componentRow[i].suitableFractionData.acceptRejectToggle ? Number(componentRow[i].suitableFractionData.unitOption.percent) : 0;
		purityWeedFraction += componentRow[i].weedFractionData.acceptRejectToggle ? Number(componentRow[i].weedFractionData.unitOption.percent) : 0;
	}
	
	requirementsTable.mainFractionData.purity = purityMainFraction;
	requirementsTable.suitableFraction.purity = puritySuitableFraction;
	requirementsTable.weedFraction.purity = purityWeedFraction;
	
	pureInpStart.value = Number(requirementsTable.mainFractionData.purity).toFixed(2);
	pureInpGood.value = Number(requirementsTable.suitableFraction.purity).toFixed(2);
	pureInpTrash.value = Number(requirementsTable.weedFraction.purity).toFixed(2);
}
function checkSuitableFractionExit(){
	if(Sustatment.ColumnState[0] == "lock"){
		if((requirementsTable.suitableFraction.mass / requirementsTable.mainFractionData.mass * 100) > Number(requirementsMaxExit("suitableFractionData"))){
			requirementsTable.suitableFraction.mass = requirementsTable.mainFractionData.mass / 100 * Number(requirementsMaxExit("suitableFractionData"));
			requirementsTable.suitableFraction.mass = Number(requirementsTable.suitableFraction.mass).toFixed(3);
		}
	}
}
function checkWeedFractionExit(){
	if(Sustatment.ColumnState[0] == "lock"){
		if((requirementsTable.weedFraction.mass / requirementsTable.mainFractionData.mass * 100) > Number(requirementsMaxExit("weedFractionData"))){
			requirementsTable.weedFraction.mass = requirementsTable.mainFractionData.mass / 100 * Number(requirementsMaxExit("weedFractionData"));
			requirementsTable.weedFraction.mass = Number(requirementsTable.weedFraction.mass).toFixed(3);
		}
	}
}
function requirementsMassUpdate(){
	var sustamentID = Sustatment.ColumnState.indexOf("active");
	switch(sustamentID){
		case 0:
			outputStart.value = outputStart.value < 0 ? Number(requirementsTable.mainFractionData.mass).toFixed(3) : Number(outputStart.value).toFixed(3);
			requirementsTable.mainFractionData.mass = Number(outputStart.value);
			if(Sustatment.ColumnState[1] == "lock" && Sustatment.ColumnState[2] == "lock"){			
				requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass / 100 * requirementsTable.suitableFraction.percent_exit);
				requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass / 100 * requirementsTable.weedFraction.percent_exit);
				
				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
			}
			else if(Sustatment.ColumnState[1] == "unlock"){
				requirementsTable.suitableFraction.mass += Number(requirementsTable.mainFractionData.mass - requirementsTable.suitableFraction.mass - requirementsTable.weedFraction.mass);
				if(requirementsTable.suitableFraction.mass < 0){
					requirementsTable.mainFractionData.mass = Number(requirementsTable.mainFractionData.mass) - Number(requirementsTable.suitableFraction.mass);
					outputStart.value = Number(requirementsTable.mainFractionData.mass).toFixed(3);
					requirementsTable.suitableFraction.mass = 0;
				}
				
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.suitableFraction.mass / requirementsTable.mainFractionData.mass * 100).toFixed(2);
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.suitableFraction.percent_exit).toFixed(2);

				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			}
			else{
				requirementsTable.weedFraction.mass += Number(requirementsTable.mainFractionData.mass - requirementsTable.weedFraction.mass - requirementsTable.suitableFraction.mass);
				if(requirementsTable.weedFraction.mass < 0){
					requirementsTable.mainFractionData.mass = Number(requirementsTable.mainFractionData.mass) - Number(requirementsTable.weedFraction.mass);
					outputStart.value = Number(requirementsTable.mainFractionData.mass).toFixed(3);
					requirementsTable.weedFraction.mass = 0;
				}
				
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.weedFraction.mass / requirementsTable.mainFractionData.mass * 100).toFixed(2);
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.weedFraction.percent_exit).toFixed(2);
				
				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			}
			break;
		case 1:
			outputGood.value = outputGood.value < 0 ? Number(requirementsTable.suitableFraction.mass).toFixed(3) : Number(outputGood.value).toFixed(3);
			requirementsTable.suitableFraction.mass = Number(outputGood.value);
			//Проверка максимального выхода
			checkSuitableFractionExit();
			if(Sustatment.ColumnState[0] == "unlock"){
				requirementsTable.mainFractionData.mass += Number(requirementsTable.suitableFraction.mass - requirementsTable.mainFractionData.mass + requirementsTable.weedFraction.mass);
				outputStart.value = Number(requirementsTable.mainFractionData.mass).toFixed(3);
				
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.suitableFraction.mass / requirementsTable.mainFractionData.mass * 100).toFixed(2) : 0;
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.suitableFraction.percent_exit).toFixed(2) : 0;

				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			} 
			else{
				requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass - requirementsTable.suitableFraction.mass);
				if(requirementsTable.weedFraction.mass < 0){
					requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass);
					outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
					requirementsTable.weedFraction.mass = 0;
				}
				
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.weedFraction.mass / requirementsTable.mainFractionData.mass * 100).toFixed(2) : 0;
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.weedFraction.percent_exit).toFixed(2) : 0;
				
				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2)
			}
			break;
		case 2:
			outputTrash.value = outputTrash.value < 0 ? Number(requirementsTable.weedFraction.mass).toFixed(3) : Number(outputTrash.value).toFixed(3);
			requirementsTable.weedFraction.mass = Number(outputTrash.value);
			//Проверка максимального выхода
			checkWeedFractionExit();
			if(Sustatment.ColumnState[0] == "unlock"){
				requirementsTable.mainFractionData.mass += Number(requirementsTable.weedFraction.mass - requirementsTable.mainFractionData.mass + requirementsTable.suitableFraction.mass);
				outputStart.value = Number(requirementsTable.mainFractionData.mass).toFixed(3);
				
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.suitableFraction.mass / requirementsTable.mainFractionData.mass * 100).toFixed(2) : 0;
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.suitableFraction.percent_exit).toFixed(2) : 0;

				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			} 
			else{
				requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass - requirementsTable.weedFraction.mass);
				if(requirementsTable.suitableFraction.mass < 0){
					requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass);
					outputTrash.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
					requirementsTable.suitableFraction.mass = 0;
				}
				
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.suitableFraction.mass / requirementsTable.mainFractionData.mass * 100).toFixed(2) : 0;
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.mass) > 0 ? Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.suitableFraction.percent_exit).toFixed(2) : 0;

				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			}
			break;
	}
	setupFractionExit();
	//suitableFractionPercent();
}
function requirementsPercentUpdate(){
	var sustamentID = Sustatment.ColumnState.indexOf("active");
	switch(sustamentID){
		case 0:
			
			break;
		case 1:
			percentGood.value = percentGood.value < 0 ? Number(requirementsTable.suitableFraction.percent_exit).toFixed(2) : Number(percentGood.value).toFixed(2);
			requirementsTable.suitableFraction.percent_exit = Number(percentGood.value) <= requirementsMaxExit("suitableFractionData") ? Number(percentGood.value) : requirementsMaxExit("suitableFractionData");
			
			requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.suitableFraction.percent_exit);
			
			requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.suitableFraction.percent_exit);
			requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.weedFraction.percent_exit);
			
			outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
			outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
			percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
			percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			break;
		case 2:
			percentTrash.value = percentTrash.value < 0 ? Number(requirementsTable.weedFraction.percent_exit).toFixed(3) : Number(percentTrash.value).toFixed(3);
			requirementsTable.weedFraction.percent_exit = Number(percentTrash.value) <= requirementsMaxExit("weedFractionData") ? Number(percentTrash.value) : requirementsMaxExit("weedFractionData");
			
			requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.weedFraction.percent_exit);
			
			requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.suitableFraction.percent_exit);
			requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.weedFraction.percent_exit);
			
			outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
			outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
			percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
			percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			break;
	}
	setupFractionExit();
	handler(chartData);
}

function setupFractionExit(){
	var __suitable = Number(requirementsMaxExit("suitableFractionData"));
	var __weed = Number(requirementsMaxExit("weedFractionData"));
	
	var sustamentID = Sustatment.ColumnState.indexOf("active");
	switch(sustamentID){
		case 0:
			if(Number(percentGood.value) > __suitable && sustamentID == 0){
				requirementsTable.suitableFraction.percent_exit = __suitable;
				requirementsTable.weedFraction.percent_exit = Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.suitableFraction.percent_exit);
					
				requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.suitableFraction.percent_exit);
				requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.weedFraction.percent_exit);
				
				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2);
			}
			if(Number(percentTrash.value) > __weed && sustamentID == 0){
				requirementsTable.weedFraction.percent_exit = __weed;
				requirementsTable.suitableFraction.percent_exit = Number(requirementsTable.mainFractionData.percent_exit - requirementsTable.weedFraction.percent_exit);
				
				requirementsTable.suitableFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.suitableFraction.percent_exit);
				requirementsTable.weedFraction.mass = Number(requirementsTable.mainFractionData.mass / requirementsTable.mainFractionData.percent_exit * requirementsTable.weedFraction.percent_exit);
				
				outputGood.value = Number(requirementsTable.suitableFraction.mass).toFixed(3);
				outputTrash.value = Number(requirementsTable.weedFraction.mass).toFixed(3);
				percentGood.value = Number(requirementsTable.suitableFraction.percent_exit).toFixed(2);
				percentTrash.value = Number(requirementsTable.weedFraction.percent_exit).toFixed(2)
			}
			break;
		case 1:
			if(Sustatment.ColumnState[0] == "unlock"){
				for(var i = 0; i < componentRow.length; i++){
					var suitableComponentMass = Number(requirementsTable.suitableFraction.mass / 100 * componentRow[i].suitableFractionData.unitOption.percent);
					var weedComponentMass = Number(requirementsTable.weedFraction.mass / 100 * componentRow[i].weedFractionData.unitOption.percent);
					
					var mainComponentMass = suitableComponentMass + weedComponentMass;
					componentRow[i].mainFractionData.unitOption.percent = mainComponentMass / (requirementsTable.mainFractionData.mass / 100);
				}
			}
			else{
				//suitableFractionPercent();
				for(var i = 0; i < componentRow.length; i++){
					var suitableComponentMass = Number(requirementsTable.suitableFraction.mass / 100 * componentRow[i].suitableFractionData.unitOption.percent);
					var mainComponentMass = Number(requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent);
					
					var weedComponentMass = mainComponentMass - suitableComponentMass;
					componentRow[i].weedFractionData.unitOption.percent = weedComponentMass / (requirementsTable.weedFraction.mass / 100);
					
					if(componentRow[i].weedFractionData.unitOption.percent == "NaN" || componentRow[i].weedFractionData.unitOption.percent == "Infinity" || componentRow[i].weedFractionData.unitOption.percent == "-Infinity"){
						if(i == 0)
							componentRow[i].weedFractionData.unitOption.percent = 100;
						else
							componentRow[i].weedFractionData.unitOption.percent = 0;
					}
				}
			}
			break;
		case 2:
			if(Sustatment.ColumnState[0] == "unlock"){
				for(var i = 0; i < componentRow.length; i++){
					var suitableComponentMass = Number(requirementsTable.suitableFraction.mass / 100 * componentRow[i].suitableFractionData.unitOption.percent);
					var weedComponentMass = Number(requirementsTable.weedFraction.mass / 100 * componentRow[i].weedFractionData.unitOption.percent);
					
					var mainComponentMass = suitableComponentMass + weedComponentMass;
					componentRow[i].mainFractionData.unitOption.percent = mainComponentMass / (requirementsTable.mainFractionData.mass / 100);
				}
			}
			else{
				//weedFractionPercent();
				for(var i = 0; i < componentRow.length; i++){
					var weedComponentMass = Number(requirementsTable.weedFraction.mass / 100 * componentRow[i].weedFractionData.unitOption.percent);
					var mainComponentMass = Number(requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent);
					
					var suitableComponentMass = mainComponentMass - weedComponentMass;
					componentRow[i].suitableFractionData.unitOption.percent = suitableComponentMass / (requirementsTable.suitableFraction.mass / 100);
					
					if(componentRow[i].suitableFractionData.unitOption.percent == "NaN" || componentRow[i].suitableFractionData.unitOption.percent == "Infinity" || componentRow[i].suitableFractionData.unitOption.percent == "-Infinity"){
						if(i == 0)
							componentRow[i].suitableFractionData.unitOption.percent = 100;
						else
							componentRow[i].suitableFractionData.unitOption.percent = 0;
					}
				}
			}
			break;
	}
}
/*
function suitableFractionPercent(){
	var suitableFractionMass = Number(requirementsTable.mainFractionData.mass / 100 * requirementsTable.suitableFraction.percent_exit);
	for(var i = 0; i < componentRow.length; i++){
		var requirementsComponentMass = requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent;
		var fractionComponentMass = Number(suitableFractionMass/100 * componentRow[i].suitableFractionData.unitOption.percent);
		
		componentRow[i].suitableFractionData.unitOption.iterfraction_percent = Number(fractionComponentMass / requirementsComponentMass) * 100;
	}
	for(var i = 0; i < componentRow.length; i++){
		componentRow[i].weedFractionData.unitOption.iterfraction_percent = 100 - componentRow[i].suitableFractionData.unitOption.iterfraction_percent;
	}
	
	var weedFractionMass = Number(requirementsTable.mainFractionData.mass / 100 * requirementsTable.weedFraction.percent_exit);
	for(var i = 0; i < componentRow.length; i++){
		var requirementsComponentMass = requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent;
		var fractionComponentMass = Number(requirementsComponentMass / 100 *  componentRow[i].weedFractionData.unitOption.iterfraction_percent);
		componentRow[i].weedFractionData.unitOption.percent = Number(fractionComponentMass / weedFractionMass * 100).toFixed(2)
		
		if(componentRow[i].weedFractionData.unitOption.percent == "NaN" || componentRow[i].weedFractionData.unitOption.percent == "Infinity" || componentRow[i].weedFractionData.unitOption.percent == "-Infinity"){
			if(i == 0)
				componentRow[i].weedFractionData.unitOption.percent = 100;
			else
				componentRow[i].weedFractionData.unitOption.percent = 0;
		}
		componentRow[i].weedFractionData.unitOption.percent = componentRow[i].weedFractionData.unitOption.percent >= 0 ? componentRow[i].weedFractionData.unitOption.percent : 0.00;
		componentRow[i].weedFractionData.unitOption.percent = componentRow[i].weedFractionData.unitOption.percent <= 100 ? componentRow[i].weedFractionData.unitOption.percent : 100.00;
	}
}
function weedFractionPercent(){
	var weedFractionMass = Number(requirementsTable.mainFractionData.mass / 100 * requirementsTable.weedFraction.percent_exit);
	for(var i = 0; i < componentRow.length; i++){
		var requirementsComponentMass = requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent;
		var fractionComponentMass = Number(suitableFractionMass/100 * componentRow[i].weedFractionData.unitOption.percent);
		
		componentRow[i].weedFractionData.unitOption.iterfraction_percent = Number(fractionComponentMass / requirementsComponentMass) * 100;
	}
	for(var i = 0; i < componentRow.length; i++){
		componentRow[i].suitableFractionData.unitOption.iterfraction_percent = 100 - componentRow[i].weedFractionData.unitOption.iterfraction_percent;
	}
	
	var suitableFractionMass = Number(requirementsTable.mainFractionData.mass / 100 * requirementsTable.suitableFraction.percent_exit);
	for(var i = 0; i < componentRow.length; i++){
		var requirementsComponentMass = requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent;
		var fractionComponentMass = Number(requirementsComponentMass / 100 *  componentRow[i].suitableFractionData.unitOption.iterfraction_percent);
		componentRow[i].suitableFractionData.unitOption.percent = Number(fractionComponentMass / weedFractionMass * 100).toFixed(2);
		
		if(componentRow[i].suitableFractionData.unitOption.percent == "NaN" || componentRow[i].suitableFractionData.unitOption.percent == "Infinity" || componentRow[i].suitableFractionData.unitOption.percent == "-Infinity"){
			if(i == 0)
				componentRow[i].suitableFractionData.unitOption.percent = 100;
			else
				componentRow[i].suitableFractionData.unitOption.percent = 0;
		}
		componentRow[i].suitableFractionData.unitOption.percent = componentRow[i].suitableFractionData.unitOption.percent >= 0 ? componentRow[i].suitableFractionData.unitOption.percent : 0.00;
		componentRow[i].suitableFractionData.unitOption.percent = componentRow[i].suitableFractionData.unitOption.percent <= 100 ? componentRow[i].suitableFractionData.unitOption.percent : 100.00;
	}
}
*/

function requirementsMaxExit(fraction){
	var minFractionMass = Number(Infinity);
	for(var i = 0; i < componentRow.length; i++){
		var requirementsComponentMass = Number(requirementsTable.mainFractionData.mass / 100 * componentRow[i].mainFractionData.unitOption.percent);
		
		var maxFractionComponentMass = Number(requirementsComponentMass / Number(componentRow[i][fraction].unitOption.percent) * 100);
		
		if(maxFractionComponentMass == "NaN" || maxFractionComponentMass == "Infinity" || maxFractionComponentMass == "-Infinity")
			maxFractionComponentMass = 0;
		
		if(maxFractionComponentMass <= minFractionMass && maxFractionComponentMass != 0)
			minFractionMass = maxFractionComponentMass
	}
	//Назначение максимальнового выхода для фракции
	var fractionMaxExitPercent = minFractionMass/requirementsTable.mainFractionData.mass * 100;
	fractionMaxExitPercent = (fractionMaxExitPercent == "NaN" || fractionMaxExitPercent == "Infinity" || fractionMaxExitPercent == "-Infinity") ? 0 : fractionMaxExitPercent;
	
	return Number(fractionMaxExitPercent).toFixed(2);
}

function GetLockSustate(column_id){
    if(Sustatment.ColumnState[column_id-1] != 'active'){
        switch(column_id){
            case'1':
                Sustatment.ColumnState[0] = 'active';
                Sustatment.ColumnState[1] = 'lock';
                Sustatment.ColumnState[2] = 'unlock';
                break;
            case'2':
                Sustatment.ColumnState[0] = 'lock';
                Sustatment.ColumnState[1] = 'active';
                Sustatment.ColumnState[2] = 'unlock';
                break;
            case'3':
                Sustatment.ColumnState[0] = 'lock';
                Sustatment.ColumnState[1] = 'unlock';
                Sustatment.ColumnState[2] = 'active';
                break;
        }
        setupIMG();
    }
    
}
function setupIMG(){
    for(var i = 0; i< Sustatment.ColumnState.length; i++){
        var img = document.getElementById('Lock_' + (i+1));
        var parent = document.getElementById('fractionLockValue_' + (i+1));
        switch(Sustatment.ColumnState[i]){
            case'active':                
                parent.children[0].children[0].style.display = 'none';
                parent.children[0].children[1].style.display = 'flex';
                img.setAttribute('status', 'active');
                break;
            case'lock':
                img.style.backgroundImage = "url(/static/TestClassifier/img/classifier/lock.png)";  
                parent.children[0].children[0].style.display = 'flex';
                parent.children[0].children[1].style.display = 'none';
                img.setAttribute('status', 'lock');             
                break;
            case'unlock':
                img.style.backgroundImage = "url(/static/TestClassifier/img/classifier/unlock.png)";
                parent.children[0].children[0].style.display = 'flex';
                parent.children[0].children[1].style.display = 'none';
                img.setAttribute('status', 'unlock'); 
                break;
        }
    }
}
function CheckLockInput(el){
    var element_id = el.id.split('_')[1];
    var activeEl;
    for(var i = 0; i< Sustatment.ColumnState.length; i++){
        if(Sustatment.ColumnState[i] == 'active'){
            activeEl = i;
            break;
        }
    }
    switch(activeEl){
        case 0:            
            var activeEl = element_id;
            var passiveEl = element_id == '2' ?  '3' : '2';
            Sustatment.ColumnState[activeEl-1] =  Sustatment.ColumnState[activeEl-1]  != 'unlock' ? 'unlock' : 'lock';
            if(Sustatment.ColumnState[activeEl-1] == 'unlock' && Sustatment.ColumnState[passiveEl-1] == 'unlock'){
                Sustatment.ColumnState[passiveEl-1] = 'lock';
            } 
            break;
        case 1:
            var activeEl = element_id;
            var passiveEl = element_id == '1' ?  '3' : '1';
            Sustatment.ColumnState[activeEl-1] =  Sustatment.ColumnState[activeEl-1]  != 'unlock' ? 'unlock' : 'lock';
            Sustatment.ColumnState[passiveEl-1] =  Sustatment.ColumnState[activeEl-1]  != 'unlock' ? 'unlock' : 'lock';
            break;
        case 2:
            var activeEl = element_id;
            var passiveEl = element_id == '1' ?  '2' : '1';
            Sustatment.ColumnState[activeEl-1] =  Sustatment.ColumnState[activeEl-1]  != 'unlock' ? 'unlock' : 'lock';
            Sustatment.ColumnState[passiveEl-1] =  Sustatment.ColumnState[activeEl-1]  != 'unlock' ? 'unlock' : 'lock';
            break;
    }
    
    setupIMG();   
}

function percentCheck(value){
	if(Number(value) > 100){
		value = "100.000";
	}
	else if(value == "" || Number(value) < 0){
		value = "0.000";
	}
	return value;
}

/* 
function MathPureInpStart(){
	var pureInpStart = document.getElementById('pureInpStart');

	if(Sustatment.ColumnState[1] == 'unlock'){
        
    }
    else if(Sustatment.ColumnState[2] == 'unlock'){

    }
}
*/


// Расчетные функции для fractionMainValues
function chtoto(){
	var pureInpStart = document.getElementById('pureInpStart');// чистота % (исходное)
	var outputStart = document.getElementById('outputStart');//производительность кг/ч (исходное)
	var percentStart = document.getElementById('percentStart');
	var pureInpGood = document.getElementById('pureInpGood');// чистота % (годное)
	var outputGood = document.getElementById('outputGood');//производительность кг/ч (годное)
	var percentGood = document.getElementById('percentGood');
	var pureInpTrash = document.getElementById('pureInpTrash');// чистота % (отход)
	var outputTrash = document.getElementById('outputTrash');//производительность кг/ч (отход)
	var percentTrash = document.getElementById('percentTrash');

	//строка производительность кг/ч
	if(outputGood.value != 0 && outputTrash.value != 0){
		outputStart.value = Number(outputGood.value) + Number(outputTrash.value);
	}
	if(outputStart.value != 0 && outputTrash.value != 0){
		outputGood.value = Number(outputStart.value) - Number(outputTrash.value);
	}
	if(outputStart.value != 0 && outputGood.value != 0){
		outputTrash.value = Number(outputStart.value) - Number(outputGood.value);
	}
	//строка  чистота % 
	// pureInpStart = 
}
