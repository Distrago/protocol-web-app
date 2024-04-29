var list_machine = []
var list_configuration = []
var list_manager = []


//Новая версия
function get_protocolData(id){
	overlay.style.display = "flex";
	$.post($SCRIPT_ROOT + '/protocol/new_get_protocol',{
		id_protocol: id
	}, function(data){
		//ProtocolData
		setupProtocolData(data.result.ProtocolData);
		setupProductData(data.result.ProtocolData);
		setupSortingData(data.result.ProtocolData);
		setupAcceptRejectData(data.result.ProtocolData);
		setupProtocolComponentData(data.result.ProtocolData);
		//RequrementsData
		setupRequrementsData(data.result.RequrementsData);
		setupFractionsData(data.result.RequrementsData);
		setupRequrementsComponentData(data.result.RequrementsData);
		
		overlay.style.display = "none";
		reviewTitle();
		reviewSourceDate();
		reviewFractionDate();
		sortingDiagram();
		console.log("Данные получены!");
	})
	.fail(function(){
		//get_protocolData(id);
	});
}
//ProtocolData
function setupProtocolData(data){
	protocol.id_protocol = data.protocol[0].ID_Protocol;
	protocol.id_requirements = data.protocol[0].ID_Requirements;
	protocol.id_creater = data.protocol[0].ID_creater;
	protocol.id_responsible = data.protocol[0].ID_responsible;
	protocol.company_name = data.protocol[0].company_name;
	protocol.equipment_machine = data.protocol[0].equipment;
	protocol.configuration = data.protocol[0].configuration;
	protocol.create_date = data.protocol[0].create_date;
	
	for(var i = 0; i < Number(data.protocol[0].componentValue); i++)
		generateProtocolComponents();
	for(var i = 0; i < Number(data.protocol[0].sortingValue); i++)
		generateProtocolSorting()
}
function setupProductData(data){
	protocol.sourceProduct.name = data.product[0].productName;
	protocol.sourceProduct.purity = Number(data.product[0].purity).toFixed(3);
	protocol.sourceProduct.capacity = Number(data.product[0].capacity_type) == 0 ? 
									Number(data.product[0].capacity).toFixed(3) : Number(data.product[0].capacity * 1000).toFixed(3);	
			
	if(Number(data.product[0].ID_mainPhoto) >= 0){
		var id = Number(data.product[0].ID_mainPhoto)+1;
		protocol.sourceProduct.image 
			= "/static/img/save_img/protocol_"+data.product[0].ID_Protocol+"/"+data.product[0].photoFolder+"/sourceProductImage_"+id+".png?u=" + last_updated;
	}
	else{
		protocol.sourceProduct.image = "/static/img/result/test.jpg";
	}
}
function setupSortingData(data){
	for(var i = 0; i< protocol.sorting.length; i++){
		protocol.sorting[i].capacity =  Number(data.sorting[i].capacity_type) == 0 ? Number(data.sorting[i].capacity) :  Number(data.sorting[i].capacity) * 1000;
		protocol.sorting[i].inbox_fraction = inbox_fraction_decode(data.sorting[i].inbox_fraction);
		protocol.sorting[i].trays_number = Number(data.sorting[i].trays_number).toFixed(2);
	}
}
function setupAcceptRejectData(data){
	for(var i = 0; i< protocol.sorting.length; i++){
		//Парамаетры прохода
		protocol.sorting[i].accept_name = data.accept[i].fractionName;
		protocol.sorting[i].accept_name_id = data.accept[i].fractionNameID;
		protocol.sorting[i].accept_exit = Number(data.accept[i].exit).toFixed(3);
		protocol.sorting[i].accept_purity = Number(data.accept[i].purity).toFixed(3);
		protocol.sorting[i].accept_mass = Number(data.accept[i].capacity).toFixed(3);
		//Параметры отбоя
		protocol.sorting[i].reject_name = data.reject[i].fractionName;
		protocol.sorting[i].reject_name_id = data.reject[i].fractionNameID;
		protocol.sorting[i].reject_exit = Number(data.reject[i].exit).toFixed(3);
		protocol.sorting[i].reject_purity = Number(data.reject[i].purity).toFixed(3);
		protocol.sorting[i].reject_mass = Number(data.reject[i].capacity).toFixed(3);
		
		//Добавляем записанные фотко для прохода
		if(Number(data.accept[i].ID_mainPhoto) >= 0){
			var id = Number(data.accept[i]["ID_mainPhoto"])+1;
			protocol.sorting[i].accept_img 
				= "/static/img/save_img/protocol_"+data.accept[i].ID_Protocol+"/"+data.accept[i].photoFolder+"/acceptImage_"+id+".png?u=" + last_updated;
		}
		else{
			protocol.sorting[i].accept_img = "/static/img/result/test.jpg";
		}
		//Добавляем записанные фотко для отбоя
		if(Number(data.reject[i].ID_mainPhoto) >= 0){
			var id = Number(data.reject[i].ID_mainPhoto)+1;
			protocol.sorting[i].reject_img 
				= "/static/img/save_img/protocol_"+data.reject[i].ID_Protocol+"/"+data.reject[i].photoFolder+"/rejectImage_"+id+".png?u=" + last_updated;
		}
		else{
			protocol.sorting[i].reject_img = "/static/img/result/test.jpg";
		}
	}
}
function setupProtocolComponentData(data){
	for(var i=0; i < protocol.sourceProduct.components.length; i++){
		protocol.sourceProduct.components[i].product_name = data.components[i][3];
		protocol.sourceProduct.components[i].value = Number(data.components[i][4]).toFixed(3);
		protocol.sourceProduct.components[i].flag_1 = (data.components[i][6] == "TRUE") ? true : false;
		protocol.sourceProduct.components[i].flag_2 = (data.components[i][7] == "TRUE") ? true : false;
		//Добавляем записанные фотки
		if(Number(data.components[i][9]) >= 0){
			var id = Number(data.components[i][9])+1;
			protocol.sourceProduct.components[i].image 
				= "/static/img/save_img/protocol_"+data.components[i][0]+"/"+data.components[i][8]+"/component_"+id+".png?u=" + last_updated; 
		}
		else{
			protocol.sourceProduct.components[i].image = "/static/img/result/test.jpg";
		}
						
		for(var j=0; j < protocol.sorting.length; j++){
			var accept_value = Number(data.components[i][(j*8+10)]).toFixed(3);
			var accept_flag_1 = (data.components[i][(j*8+12)] == "TRUE") ? true : false;
			var accept_flag_2 = (data.components[i][(j*8+13)] == "TRUE") ? true : false;
			protocol.sorting[j].accept_components[i] = {
				product_name: data.components[i][3],
				value: Number(accept_value).toFixed(3),
				flag_1: accept_flag_1,
				flag_2: accept_flag_2
			};
			var reject_value = Number(data.components[i][(j*8+14)]).toFixed(3);
			var reject_flag_1 = (data.components[i][(j*8+16)] == "TRUE") ? true : false;
			var reject_flag_2 = (data.components[i][(j*8+17)] == "TRUE") ? true : false;
			protocol.sorting[j].reject_components[i] = {
				product_name: data.components[i][3],
				value: Number(reject_value).toFixed(3),
				flag_1: reject_flag_1,
				flag_2: reject_flag_2
			};
		}
	}
}
//RequrementsData
function setupRequrementsData(data){
	requirements.id_requirements = data.requirements[0].ID_requirements;
	
	var capacity_value = Number(data.requirements[0].capacity_value);
	var capacity_type = data.requirements[0].capacity_type;
	var time_value = Number(data.requirements[0].time_value);
	var time_type = data.requirements[0].time_type;
	var hour_in_day = data.requirements[0].hour_in_day;
	var day_in_week = data.requirements[0].day_in_week;
	var month_in_year = data.requirements[0].month_in_year;
		
	switch(Number(time_type)){
	case 0:
		requirements.capacity = Number(capacity_value / time_value);
		break;
	case 1:
		var hour = time_value * hour_in_day;
		requirements.capacity = Number(capacity_value / hour);
		break;
	case 2:
		var week = (time_value * 30/7);
		var day = day_in_week * week;
		var hour = hour_in_day * day;
		requirements.capacity = Number(capacity_value / hour);
		break;
	case 3:
		var month = (time_value * month_in_year);
		var week = (month * 30/7);
		var day = day_in_week * week;
		var hour = hour_in_day * day;
		requirements.capacity = Number(capacity_value / hour);
		break;
	}
	
	requirements.capacity = capacity_type == 0 ? requirements.capacity * 1000 : requirements.capacity;
	requirements.capacity = Number(requirements.capacity).toFixed(3);
	
	var fraction_count = Number(data.requirements[0].fraction_count);
	var companent_count = Number(data.requirements[0].companent_count);
		
	//Создать необходимое число фракций и компонентов
	for(var i = 0; i < fraction_count; i++)
		generateRequirementsFractions();
	for(var i = 0; i < companent_count; i++)
		generateRequirementsComponents();
}
function setupFractionsData(data){
	for(var i = 0 ; i < data.fraction.length; i++){
		requirements.fractions[i].fractionName = data.fraction[i].fraction_name;
		requirements.fractions[i].purpose = Number(data.fraction[i].purpose);
		requirements.fractions[i].exit = Number(data.fraction[i].exit).toFixed(3);
		requirements.fractions[i].purity = Number(data.fraction[i].purity).toFixed(3);
		requirements.fractions[i].capacity = Number(data.fraction[i].capacity).toFixed(3);
		
		requirements.fractions[i].image 
			= "/static/img/save_img/requirement_"+data.fraction[i].ID_requirements+"/"+data.fraction[i].photoFolder+"/fraction_"+data.fraction[i].ID_mainPhoto+".png?u=" + last_updated;
	}
}
function setupRequrementsComponentData(data){
	requirements.purity = 0;
	for(var i = 0; i < data.components.length; i++){
		requirements.components[i].product_name = data.components[i][2];
		requirements.components[i].value =  Number(data.components[i][4]).toFixed(3);
		requirements.components[i].flag_1 = (data.components[i][6] == "TRUE") ? true : false;
		requirements.components[i].flag_2 = (data.components[i][7] == "TRUE") ? true : false;
		requirements.purity += requirements.components[i].flag_1 ? Number(requirements.components[i].value) : 0;
		
		requirements.components[i].image = "/static/img/save_img/requirement_"+data.components[i][01]+"/"+data.components[i][8]+"/component_"+data.components[i][9]+".png?u=" + last_updated;
		
		for(var k = 0; k < requirements.fractions.length; k++){
			requirements.fractions[k].components[i].product_name = data.components[i][2];
			requirements.fractions[k].components[i].value =  Number(data.components[i][(10+4*k)]).toFixed(3);
			requirements.fractions[k].components[i].flag_1 = (data.components[i][(12+4*k)] == "TRUE") ? true : false;
			requirements.fractions[k].components[i].flag_2 = (data.components[i][(13+4*k)] == "TRUE") ? true : false;
		}
	}
	requirements.purity = Number(requirements.purity).toFixed(3);
}
//Старая версия
function get_protocol(id){
	overlay.style.display = "flex";
	$.post($SCRIPT_ROOT + '/protocol/get_protocol_result',{
		id_protocol: id
	}, function(data){
		protocol.id_protocol = data.result[0]["ID_Protocol"];
		protocol.id_requirements = data.result[0]["ID_Requirements"];
		protocol.id_creater = data.result[0]["ID_creater"];
		protocol.id_responsible = data.result[0]["ID_responsible"];
		protocol.company_name = data.result[0]["company_name"];
		protocol.equipment_machine = data.result[0]["equipment"];
		protocol.configuration = data.result[0]["configuration"];
		protocol.create_date = data.result[0]["create_date"];
	
		for(var i = 0; i < Number(data.result[0]["componentValue"]); i++)
			generateProtocolComponents();
		for(var i = 0; i < Number(data.result[0]["sortingValue"]); i++)
			generateProtocolSorting();
		get_product();
	})
	.fail(function(){
		get_protocol(id);
	});
}

function get_product(){
	$.getJSON($SCRIPT_ROOT + '/protocol/get_product',{
	}, function(data){
		protocol.sourceProduct.name = data.result[0]["productName"];
		protocol.sourceProduct.purity = Number(data.result[0]["purity"]).toFixed(3);
		protocol.sourceProduct.capacity = Number(data.result[0]["capacity_type"]) == 0 ? Number(data.result[0]["capacity"]).toFixed(3) : Number(data.result[0]["capacity"] * 1000).toFixed(3);	
			
		if(Number(data.result[0]["ID_mainPhoto"]) >= 0){
			var id = Number(data.result[0]["ID_mainPhoto"])+1;
			protocol.sourceProduct.image 
				= "/static/img/save_img/protocol_"+data.result[0].ID_Protocol+"/"+data.result[0].photoFolder+"/sourceProductImage_"+id+".png?u=" + last_updated;
		}
		else{
			protocol.sourceProduct.image = "/static/img/result/test.jpg";
		}
		get_sorting();
	})
	.fail(function(){
		get_product();
	});
}
function get_sorting(){
	$.getJSON($SCRIPT_ROOT + '/protocol/get_sorting',{
	}, function(data){
		for(var i = 0; i< protocol.sorting.length; i++){
			protocol.sorting[i].capacity =  Number(data.result[i]["capacity_type"]) == 0 ? Number(data.result[i]["capacity"]) :  Number(data.result[i]["capacity"]) * 1000;
			protocol.sorting[i].inbox_fraction = inbox_fraction_decode(data.result[i]["inbox_fraction"]);
			protocol.sorting[i].trays_number = Number(data.result[i]["trays_number"]).toFixed(2);
		}
		get_accept();
	})
	.fail(function(){
		get_sorting();
	});
}
function get_accept(){
	$.getJSON($SCRIPT_ROOT + '/protocol/get_accept',{
	}, function(data){
		var count = 0;
		for(var i = 0; i< protocol.sorting.length; i++){
			protocol.sorting[i].accept_name = data.result[count]["fractionName"];
			protocol.sorting[i].accept_name_id = data.result[count]["fractionNameID"];
			protocol.sorting[i].accept_exit = Number(data.result[count]["exit"]).toFixed(3);
			protocol.sorting[i].accept_purity = Number(data.result[count]["purity"]).toFixed(3);
			protocol.sorting[i].accept_mass = Number(data.result[count]["capacity"]).toFixed(3);
			//Добавляем записанные фотки
			if(Number(data.result[count]["ID_mainPhoto"]) >= 0){
				var id = Number(data.result[count]["ID_mainPhoto"])+1;
				protocol.sorting[i].accept_img 
					= "/static/img/save_img/protocol_"+data.result[i].ID_Protocol+"/"+data.result[i].photoFolder+"/acceptImage_"+id+".png?u=" + last_updated;
			}
			else{
				protocol.sorting[i].accept_img = "/static/img/result/test.jpg";
			}
			count++;
		}
		get_reject();
	})
	.fail(function(){
		get_accept();
	});
}

function get_reject(){
	$.getJSON($SCRIPT_ROOT + '/protocol/get_reject',{
	}, function(data){
		var count = 0;
		for(var i = 0; i< protocol.sorting.length; i++){
			protocol.sorting[i].reject_name = data.result[count]["fractionName"];
			protocol.sorting[i].reject_name_id = data.result[count]["fractionNameID"];
			protocol.sorting[i].reject_exit = Number(data.result[count]["exit"]).toFixed(3);
			protocol.sorting[i].reject_purity = Number(data.result[count]["purity"]).toFixed(3);
			protocol.sorting[i].reject_mass = Number(data.result[count]["capacity"]).toFixed(3);
			//Добавляем записанные фотки
			
			if(Number(data.result[count]["ID_mainPhoto"]) >= 0){
				var id = Number(data.result[count]["ID_mainPhoto"])+1;
				protocol.sorting[i].reject_img 
					= "/static/img/save_img/protocol_"+data.result[i].ID_Protocol+"/"+data.result[i].photoFolder+"/rejectImage_"+id+".png?u=" + last_updated;
			}
			else{
				protocol.sorting[i].reject_img = "/static/img/result/test.jpg";
			}
			
			count++;
		}
		get_component();
	})
	.fail(function(){
		get_reject();
	});
}
function get_component(){
	$.getJSON($SCRIPT_ROOT + '/protocol/get_component',{
	}, function(data){
		var count = 0;
		for(var i=0; i < protocol.sourceProduct.components.length; i++){
			protocol.sourceProduct.components[i].product_name = data.result[count]["row_3"];
			protocol.sourceProduct.components[i].value = Number(data.result[count]["row_4"]).toFixed(3);
			protocol.sourceProduct.components[i].flag_1 = (data.result[count]["row_6"] == "TRUE") ? true : false;
			protocol.sourceProduct.components[i].flag_2 = (data.result[count]["row_7"] == "TRUE") ? true : false;
			//Добавляем записанные фотки
			if(Number(data.result[count]["row_9"]) >= 0){
				var id = Number(data.result[count]["row_9"])+1;
				protocol.sourceProduct.components[i].image 
					= "/static/img/save_img/protocol_"+data.result[count].row_0+"/"+data.result[count].row_8+"/component_"+id+".png?u=" + last_updated; 
			}
			else{
				protocol.sourceProduct.components[i].image = "/static/img/result/test.jpg";
			}
						
			for(var j=0; j < protocol.sorting.length; j++){
				var accept_value = Number(data.result[count]["row_"+(j*8+10)]).toFixed(3);
				var accept_flag_1 = (data.result[count]["row_"+(j*8+12)] == "TRUE") ? true : false;
				var accept_flag_2 = (data.result[count]["row_"+(j*8+13)] == "TRUE") ? true : false;
				protocol.sorting[j].accept_components[i] = {
					product_name: data.result[count].row_3,
					value: Number(accept_value).toFixed(3),
					flag_1: accept_flag_1,
					flag_2: accept_flag_2
				};
				var reject_value = Number(data.result[count]["row_"+(j*8+14)]).toFixed(3);
				var reject_flag_1 = (data.result[count]["row_"+(j*8+16)] == "TRUE") ? true : false;
				var reject_flag_2 = (data.result[count]["row_"+(j*8+17)] == "TRUE") ? true : false;
				protocol.sorting[j].reject_components[i] = {
					product_name: data.result[count].row_3,
					value: Number(reject_value).toFixed(3),
					flag_1: reject_flag_1,
					flag_2: reject_flag_2
				};
			}
			count++;
		}
		get_requirements();
	})
	.fail(function(){
		get_component();
	});
}

function get_requirements(){
	$.post($SCRIPT_ROOT + '/protocol/requirements/get_requirements',{
		id_requirements: protocol.id_requirements
	}, function(data){
		requirements.id_requirements = data.result[0]["ID_requirements"];
		
		var capacity_value = Number(data.result[0]["capacity_value"]);
		var capacity_type = data.result[0]["capacity_type"];
		var time_value = Number(data.result[0]["time_value"]);
		var time_type = data.result[0]["time_type"];
		var hour_in_day = data.result[0]["hour_in_day"]
		var day_in_week = data.result[0]["day_in_week"]
		var month_in_year = data.result[0]["month_in_year"]
		
		switch(Number(time_type)){
		case 0:
			requirements.capacity = Number(capacity_value / time_value);
			break;
		case 1:
			var hour = time_value * hour_in_day;
			requirements.capacity = Number(capacity_value / hour);
			break;
		case 2:
			var week = (time_value * 30/7);
			var day = day_in_week * week;
			var hour = hour_in_day * day;
			requirements.capacity = Number(capacity_value / hour);
			break;
		case 3:
			var month = (time_value * month_in_year);
			var week = (month * 30/7);
			var day = day_in_week * week;
			var hour = hour_in_day * day;
			requirements.capacity = Number(capacity_value / hour);
			break;
		}
		
		requirements.capacity = capacity_type == 0 ? requirements.capacity * 1000 : requirements.capacity;
		requirements.capacity = Number(requirements.capacity).toFixed(3);
		
		var fraction_count = Number(data.result[0]["fraction_count"]);
		var companent_count = Number(data.result[0]["companent_count"]);
			
		//Создать необходимое число фракций и компонентов
		for(var i = 0; i < fraction_count; i++)
			generateRequirementsFractions();
		for(var i = 0; i < companent_count; i++)
			generateRequirementsComponents();
		
		get_requirements_fractions();
	})
	.fail(function(){
		get_requirements()
	});
}
function get_requirements_fractions(){
	$.getJSON($SCRIPT_ROOT + '/protocol/requirements/get_fraction',{
	}, function(data){
		for(var i = 0 ; i < data.result.length; i++){
			requirements.fractions[i].fractionName = data.result[i]["fraction_name"]
			requirements.fractions[i].purpose = Number(data.result[i]["purpose"]);
			requirements.fractions[i].exit = Number(data.result[i]["exit"]).toFixed(3);
			requirements.fractions[i].purity = Number(data.result[i]["purity"]).toFixed(3);
			requirements.fractions[i].capacity = Number(data.result[i]["capacity"]).toFixed(3);
			
			requirements.fractions[i].image 
				= "/static/img/save_img/requirement_"+data.result[i]["ID_requirements"]+"/"+data.result[i]["photoFolder"]+"/fraction_"+data.result[i]["ID_mainPhoto"]+".png?u=" + last_updated;
		}
		get_requirements_components();
	})
	.fail(function(){
		get_requirements_fractions()
	});
}
function get_requirements_components(){
	$.getJSON($SCRIPT_ROOT + '/protocol/requirements/get_component',{
	}, function(data){
		requirements.purity = 0;
		for(var i = 0; i < data.result.length; i++){
			requirements.components[i].product_name = data.result[i]["row_2"];
			requirements.components[i].value =  Number(data.result[i]["row_4"]).toFixed(3);
			requirements.components[i].flag_1 = (data.result[i]["row_6"] == "TRUE") ? true : false;
			requirements.components[i].flag_2 = (data.result[i]["row_7"] == "TRUE") ? true : false;
			requirements.purity += requirements.components[i].flag_1 ? Number(requirements.components[i].value) : 0;
			
			requirements.components[i].image = "/static/img/save_img/requirement_"+data.result[i]["row_0"]+"/"+data.result[i]["row_8"]+"/component_"+data.result[i]["row_9"]+".png?u=" + last_updated;
			
			for(var k = 0; k < requirements.fractions.length; k++){
				requirements.fractions[k].components[i].product_name = data.result[i]["row_2"];
				requirements.fractions[k].components[i].value =  Number(data.result[i]["row_"+(10+4*k)]).toFixed(3);
				requirements.fractions[k].components[i].flag_1 = (data.result[i]["row_"+(12+4*k)] == "TRUE") ? true : false;
				requirements.fractions[k].components[i].flag_2 = (data.result[i]["row_"+(13+4*k)] == "TRUE") ? true : false;
			}
		}
		requirements.purity = Number(requirements.purity).toFixed(3);
		read_machine();
	})
	.fail(function(){
		get_requirements_components()
	});
}
function inbox_fraction_decode(split_string){
	var decode_array = []
	for(var i=0; i<split_string.length; i += 2){
		if (split_string.slice(i,i+2) == "00")
			decode_array.push({"accept": false, "reject": false});
		else if(split_string.slice(i,i+2) == "10")
			decode_array.push({"accept": true, "reject": false});
		else if(split_string.slice(i,i+2) == "01")
			decode_array.push({"accept": false, "reject": true});
		else if(split_string.slice(i,i+2) == "11")
			decode_array.push({"accept": true, "reject": true});
	}
	
	return decode_array;
}
//Получение таблиц аппаратов и конфигураций
function read_machine(){
	$.getJSON($SCRIPT_ROOT + '/protocol/classifier/machine',{	
	}, function(data){
		for(var i = 0; i< data.result.length; i++){
			list_machine.push({
				"id_machine": data.result[i]["id_machine"],
				"machineName": data.result[i]["machineName"]
			});
		}
	})
	.fail(function(){
		read_machine();
	});
}

function read_configuration(){
	$.getJSON($SCRIPT_ROOT + '/protocol/classifier/configuration',{	
	}, function(data){
		for(var i = 0; i< data.result.length; i++){
			list_configuration.push({
				"id_configuration": data.result[i]["id_configuration"],
				"configuration": data.result[i]["configuration"]                                           
			});
		}
	})
	.fail(function(){
		read_configuration();
	});
}

function read_manager(){
	$.getJSON($SCRIPT_ROOT + '/protocol/user/manager',{
	}, function(data){
		for(var i = 0; i< data.result.length; i++){
			list_manager.push({
				"id_user": data.result[i]["id_user"],
				"name": data.result[i]["name"],
				"mail": data.result[i]["mail"],
				"phone": data.result[i]["phone"],
				"rank_position": data.result[i]["rank_position"],
				"district": data.result[i]["district"]
			});
		}
	})
	.fail(function(){
		read_manager();
	})
}
function search_user_info(id_user){
	for(var i=0; i < list_manager.length; i++){
		if(id_user == list_manager[i].id_user)
			var result = list_manager[i];
	}
	
	return result;
}
