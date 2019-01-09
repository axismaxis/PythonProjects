! function () {
	var s = {
		"timestamps": {
			"13561": "1514560576"
		},
		"variations": [{
			"campaign_id": "571",
			"selector": ".canvas-page",
			"custom": "var changeOpenText = function (interval) {\r\n\tvar ncListInterval = setInterval(function () {\r\n\t\tvar storeFinder = $('.ah-store-finder');\r\n\r\n\t\tif (storeFinder.length) {\r\n\t\t\tvar nextButton = $('.ah-show-next-stores-button', storeFinder);\r\n\t\t\tvar ncCheckbox = $('.nc-checkbox-input', storeFinder);\r\n\t\t\tvar shopInput = $('.nc-google-maps-autocomplete__search-field', storeFinder);\r\n\t\t\tvar resetInput = $('.nc-google-maps-autocomplete__reset-location-button', storeFinder);\r\n\t\t\tvar localButton = $('nc-google-maps-autocomplete__current-location-button', storeFinder);\r\n\r\n\t\t\tif (nextButton.length) {\r\n\t\t\t\tnextButton.on('click', changeOpenText.bind(1));\r\n\t\t\t}\r\n\r\n\t\t\tif (ncCheckbox.length) {\r\n\t\t\t\tncCheckbox.on('click', changeOpenText.bind(1));\r\n\t\t\t}\r\n\t\t\t\r\n\t\t\tif (resetInput.length) {\r\n\t\t\t\tresetInput.on('click', changeOpenText.bind(1));\r\n\t\t\t}\r\n\t\t\t\r\n\t\t\tif (localButton.length) {\r\n\t\t\t\tlocalButton.on('click', changeOpenText.bind(1));\r\n\t\t\t}\r\n\t\t\r\n\t\t\tshopInput.change(function () {\r\n\t\t\t\tsetTimeout(function () {\r\n\t\t\t\t\tchangeOpenText(1);\r\n\t\t\t\t}, 300);\r\n\t\t\t});\r\n\r\n\t\t\t$('.ah-store__open-today', storeFinder)\r\n\t\t\t\t.css('cursor', 'pointer')\r\n\t\t\t\t.text('Klik voor openingstijden')\r\n\t\t\t\t.on('click', function () {\r\n\t\t\t\t\t$(this).siblings('.ah-store__address').trigger('click');\r\n\t\t\t\t})\t\r\n\r\n\t\t\tclearInterval(ncListInterval);\r\n\t\t}\r\n\t}, interval);\r\n};\r\n\r\nchangeOpenText(50);\r\n",
			"attributes": {},
			"id": "13561",
			"criteria": [{
				"Type": "Path",
				"path_criterion": "^/winkels"
			}],
			"counted": 0,
			"css": {}
		}]
	};
	window.ss_dom_var ? window.ss_dom_var.setVariations(s) : window.__ss_variations = s;
	if (s.control_sv_cv_rp_only) {
		window.__ss_control = true;
	};
}();