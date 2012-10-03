Ext.onReady(function() {
    
    var map, mapPanel, gridPanel, mainPanel;
    
    // create the map instance
    map = new OpenLayers.Map();
    var wmsLayer = new OpenLayers.Layer.WMS(
        "vmap0",
        "http://vmap0.tiles.osgeo.org/wms/vmap0",
        {layers: 'basic'}
    );
    
    // styles stuff for countries
    var rule_country_1 = new OpenLayers.Rule({
            filter: new OpenLayers.Filter.Comparison({
            type: OpenLayers.Filter.Comparison.EQUAL_TO,
            property: 'desk_study',
            value: 'True',
        }),
        symbolizer: {
            fillColor: "#ff0000",
            strokeColor: "#000000"
            }
    });
    var rule_country_2 = new OpenLayers.Rule({
            filter: new OpenLayers.Filter.Comparison({
            type: OpenLayers.Filter.Comparison.EQUAL_TO,
            property: 'desk_study',
            value: 'False',
        }),
        symbolizer: {
            fillColor: "#0000ff",
            strokeColor: "#000000"
            }
    });
    var country_style = new OpenLayers.Style();
    country_style.addRules([rule_country_1, rule_country_2]);
    var selectStyle = new OpenLayers.Style({
        fillColor: "#ffff00"
    });
    var country_style_Map = new OpenLayers.StyleMap({
        'default': country_style,
        'select': selectStyle});
    
    // create the vector layer
    var vecLayer = new OpenLayers.Layer.Vector("vector", { styleMap: country_style_Map });
    map.addLayers([wmsLayer, vecLayer]);
    
    // create the select feature for vector layer
    var select_options = {
        onSelect : getInfo
    };
    var select = new OpenLayers.Control.SelectFeature(vecLayer, select_options);
    map.addControl(select);
    select.activate();

    // create the map panel
    mapPanel = new GeoExt.MapPanel({
        title: 'Map',
        region: 'center',
        height: 400,
        width: 500,
        map: map,
        center: new OpenLayers.LonLat(0, 25),
        zoom: 2
    });
    
    // create feature store, binding it to the vector layer
    var feature_store = new GeoExt.data.FeatureStore({
        layer: vecLayer,
        fields: [
            {name: 'name', type: 'string'}
        ],
        proxy: new GeoExt.data.ProtocolProxy({
            protocol: new OpenLayers.Protocol.HTTP({
                url: "countries/kml",
                format: new OpenLayers.Format.KML()
            })
        }),
        autoLoad: true
    });
    
    // create the data store
    var store = new Ext.data.JsonStore({
        url: 'per-country/-1/json',
        fields: [
            {name: 'id', type: 'int'}, 'title', 'date', 'country', 'evaluation_type', 'link'
        ]
    });
    store.load();

    // create a grid to display records from the store
    gridPanel = new Ext.grid.GridPanel({
        title: "Evaluations",
        store: store,
        columns: [
            { id:'id', header: 'ID', width: 50, sortable: true, dataIndex: 'id' },
            { header: 'Title', width: 100, sortable: true, dataIndex: 'title' },
            { header: 'Date', width: 100, sortable: true, dataIndex: 'date' },
            { header: 'Country', width: 100, sortable: true, dataIndex: 'country' },
            { header: 'Evaluation Type', width: 100, sortable: true, dataIndex: 'evaluation_type' },
            { header: 'Link', width: 255, sortable: true, dataIndex: 'link' }
        ],
        region: 'east',
        width: 400
    });
    
    // create a panel and add the map panel and grid panel inside
    mainPanel = new Ext.Panel({
        renderTo: "mainpanel",
        layout: "border",
        height: 400,
        width: 920,
        items: [mapPanel, gridPanel]
    });
    
    // get country evaluations
    function getInfo(feature) {
        store.proxy.conn.url = 'per-country/' + feature.data.country_id + '/json';
        store.reload();
    }
});
