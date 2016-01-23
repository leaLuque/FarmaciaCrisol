// JavaScript Document
function menu_usuario(){
	eliminar(document.getElementById("indice"))
	
	agregar_li("» Ingresar", "id_ing", "javascript:ingresar()");
	agregar_li("» Salir", "id_salir", "javascript:salir()");
}

function menu_venta(){
	eliminar(document.getElementById("indice"))
	
	agregar_li("» Venta con Remito", "id_vent_rem", "javascript:salir()");
	agregar_li("» Registrar Cobro Remito", "id_reg_cob_rem", "javascript:salir()");
	agregar_li("» Modificar Remito", "id_mod_rem", "javascript:salir()");
	agregar_li("» Baja Remito", "id_baja_rem", "javascript:salir()");
	agregar_li("» Venta Contado", "id_vent_cont", "javascript:salir()");
	agregar_li("» Reintegro Cliente", "id_reint_clt", "javascript:salir()");
	agregar_li("» Devolución Cliente", "id_dev_clt", "javascript:salir()");
}

function menu_producto(){
	eliminar(document.getElementById("indice"))
	
	agregar_li("» Alta Producto", "id_alta_prod", "javascript:salir()");
	agregar_li("» Baja Producto", "id_baja_prod", "javascript:salir()");
	agregar_li("» Modificación Producto", "id_mod_prod", "javascript:salir()");
	agregar_li("» Alta Medicamento", "id_alta_med", "javascript:salir()");
	agregar_li("» Baja Medicamento", "id_baja_med", "javascript:salir()");
	agregar_li("» Modificación Medicamento", "id_mod_med", "javascript:salir()");
	agregar_li("» Alta Monodroga", "id_alta_mon", "javascript:salir()");
	agregar_li("» Baja Monodroga", "id_baja_mon", "javascript:salir()");
	agregar_li("» Modificación Monodroga", "id_mod_mon", "javascript:salir()");
	agregar_li("» Alta Presentación", "id_alta_pres", "javascript:salir()");
	agregar_li("» Baja Presentación", "id_baja_pres", "javascript:salir()");
	agregar_li("» Modificación Presentación", "id_mod_pres", "javascript:salir()");
	agregar_li("» Alta Lote", "id_alta_lote", "javascript:salir()");
	agregar_li("» Modificación Lote", "id_mod_lote", "javascript:salir()");
	agregar_li("» Ajuste Negativo de Stock", "id_mod_ajuste_neg_stock", "javascript:salir()");
}

function menu_cliente(){
	eliminar(document.getElementById("indice"))
	
	agregar_li("» Alta Cliente", "id_alta_clt", "javascript:salir()");
	agregar_li("» Baja Cliente", "id_baja_clt", "javascript:salir()");
	agregar_li("» Modificación Cliente", "id_mod_clt", "javascript:salir()");
}

function menu_listado(){
	eliminar(document.getElementById("indice"))
	
	agregar_li("» Generar Listados", "id_gen_list", "javascript:salir()");
}


function menu_ayuda(){
	eliminar(document.getElementById("indice"))
	
	agregar_li("» Ayuda", "id_ayuda", "javascript:salir()");
	agregar_li("» Acerca de ...", "id_acerca_de", "javascript:salir()");
}

/**
 * Funcion que añade <li> dentro del <ul>
 */
function agregar_li(txt, id, href){
	var li = document.createElement("li");
	document.getElementById("indice").appendChild(li)
	var a = document.createElement("a");
	a.innerHTML = txt;
	a.setAttribute("href", href);
	a.setAttribute("id", id);
	li.appendChild(a);
	var items = document.getElementById("indice").getElementsByTagName("li");
	if (items.length == 1){
		a.setAttribute("class", "selected");
	}
}

/**
 * Funcion para eliminar los <li> del <ul>
 */
function eliminar(lista)
{
	var items = lista.getElementsByTagName("li");
	var len = items.length;
	for (var i = 0; i < len; i++){
		items[0].remove();
	}
}

function leer_pdf(files){
	var file = files[0];
	var reader = new FileReader();
	reader.readAsText(file);
	var d = document.getElementById("parraf");
	d.setAttribute(text, "asd");
}

function ingresar(){
	document.getElementById("titulo").innerHTML = "Ingresar";
}

function salir(){
	document.getElementById("titulo").innerHTML = "Salir";
}