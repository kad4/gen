/* BBC World Service JS Library (GEL)  */

ws = {
    version: '2.1.0',  //cache version .js?...
    glowVersion: '1.7.3',
    env: {}
}

ws.config = {
    liveConfigRefreshInterval: 5 * 60 * 1000, // Every 5 mins, check for updates to the live config file,
	defaultEmpVersion: 3,
    afrique:    { 
                    multiClipEmpItems: 3, 
                    topicsAzPerPage: 50,
                    empStandardDisplayMode: {
                        selectors: '.index.genre-multimedia',
                        documents: [
                          '000000_africana_generic',
                          '000000_lautre_actualite_generic',  
                          '000000_lafrique_direct_generic',
                          '000000_britannia_generic',
                          '000000_palabres_generic',
                          '000000_club_bbc_generic',
                          '000000_afrique_hebdo_generic',
                          '000000_linterview_generic',
                          '000000_sports_weekend_generic',
						  '000000_a_vous_l_antenne_one',
						  '000000_a_vous_l_antenne_two',
						  '000000_grand_reportage',
						  '000000_chronique_foot',
						  '000000_le_journal_de_la_culture',
						  '000000_multi_sports_part_1',
						  '000000_multi_sports_part_2',
						  '000000_cest_le_moment',
						  '000000_best_of_a_vous_lantenne'
                      ]                     
                    },
                    empFontSupported: false
                },
    arabic_1024:     { 
                    sampleText: 'الصفحة الرئيسية الشرق الأوسط',
                    topicsAzPerPage: 50,
					empFontSupported: false,
					tmOpenFromHourGMT: 00,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 23,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 21,
					tmClosedDate: 26,
					tmOpenMonth: 1, 
					tmClosedMonth: 1, 
					tmOpenYear: 2013,
					tmClosedYear: 2013,
					tmMaxTweets: 20
                },                
    azeri:      {	empFontSupported: false },
    bengali:    { 
                    multiClipEmpItems: 6, 
                    sampleText: 'বিশেষ আয়োজন',
					empFontSupported: false
                },
    burmese:    {   
					sampleText: 'ဝဲ‌ေတမ္ဟု ရ္ဝယ္‌',
					empFontSupported: false
				},
    gel:        {   multiClipEmpItems: 3 },
    greatlakes: {   
					multiClipEmpItems: 3,
					empFontSupported: false
				},
    hausa:      {   
					multiClipEmpItems: 4,
					tmOpenFromHourGMT: 08,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 07,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 22,
					tmClosedDate: 15,
					tmOpenMonth: 6, 
					tmClosedMonth: 7, 
					tmOpenYear: 2012,
					tmClosedYear: 2012,
					tmMaxTweets: 20
				},
    hindi:      {   
					sampleText: 'चुनाव 2014:  ट्विटर अपडेट' ,
					tmOpenFromHourGMT: 14,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 23,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 23,
					tmClosedDate: 28,
					tmOpenMonth: 5,
					tmClosedMonth: 5, 
					tmOpenYear: 2014,
					tmClosedYear: 2014,
					tmMaxTweets: 20
				},
    indonesia:  {   multiClipEmpItems: 3, 
					rollingNewsVisibleItems:4
				},
    kyrgyz:     {	empFontSupported: false },
    mundo:    	{   
					multiClipEmpItems: 3, 
					rollingNewsVisibleItems:3,
					listingThresholdHours:4,
					rollingnewsThresholdHours:4,
					pageThresholdHours:4,
					pageRelativeDatestamp:true,
					defaultDisplayTimeAfterThreshold:false,
					tmOpenFromHourGMT: 00,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 23,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 27,
					tmClosedDate: 12,
					tmOpenMonth: 9, 
					tmClosedMonth: 10, 
					tmOpenYear: 2012,
					tmClosedYear: 2012,
					tmMaxTweets: 20
				},
    nepali:     {   multiClipEmpItems: 3, empFontSupported: false },
    pashto:     {   multiClipEmpItems: 5, empFontSupported: false },
    persian:    {   
					rollingNewsVisibleItems:4,
					sampleText: 'بی بی سی مسئول محتوای سایت های دیگر نیست',
					empFontSupported: false,
					tmOpenFromHourGMT: 00,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 10,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 29,
					tmClosedDate: 12,
					tmOpenMonth: 9,
					tmClosedMonth: 1, 
					tmOpenYear: 2012,
					tmClosedYear: 2015,
					tmMaxTweets: 40
				}, 
	portuguese:	{   
					multiClipEmpItems: 3,
					empLang: 'pt',
					tmOpenFromHourGMT: 08,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 07,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 22,
					tmClosedDate: 15,
					tmOpenMonth: 6, 
					tmClosedMonth: 7, 
					tmOpenYear: 2012,
					tmClosedYear: 2012,
					tmMaxTweets: 20
				},
    russian_1024:    {   multiClipEmpItems: 3 },
    sinhala: {   
					multiClipEmpItems: 3,
					empFontSupported: false
				},
    somali:     {   multiClipEmpItems: 4 },
    swahili:    {   multiClipEmpItems: 4 },
    tamil:      {   multiClipEmpItems: 4,
                    empStandardDisplayMode: {
                        selectors: '.index.genre-multimedia',
                        documents: [
                          '000000_bulletin',
                          '000000_prog_fm',  
                          '000000_prog_sunday',
                          '000000_prog_saturday',
                          '000000_prog_friday',
                          '000000_prog_thursday',
                          '000000_prog_wednesday',
                          '000000_prog_tuesday',
                          '000000_prog_monday',
                          '000000_programme_overwrite'
                      ]                     
                    },
					empFontSupported: false					
                },
    turkish:    {   
					multiClipEmpItems: 3,
					tmOpenFromHourGMT: 08,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 07,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 26,
					tmClosedDate: 27,
					tmOpenMonth: 1, 
					tmClosedMonth: 1, 
					tmOpenYear: 2014,
					tmClosedYear: 2015,
					tmMaxTweets: 20    
				},
    russian:    {   
					multiClipEmpItems: 3,
					rollingNewsVisibleItems:3,
					tmOpenFromHourGMT: 00,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 23,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 21,
					tmClosedDate: 25,
					tmOpenMonth: 1,
					tmClosedMonth: 2, 
					tmOpenYear: 2014,
					tmClosedYear: 2015,
					tmMaxTweets: 20
				},
    russian_liveplanet:    {   multiClipEmpItems: 3, rollingNewsVisibleItems:4,
								moreMultimediaDefaultTabs: {
									'Животные': '.genre-animals',
									'Среда обитания': '.genre-habitat',
									'Поведение': '.genre-behaviour'
								},
								empHighlightColour: '0x78B200'
							},
	tajik: 		{	empFontSupported: false },
	ukrainian:	{   multiClipEmpItems: 3, 
					tmOpenFromHourGMT: 00,
					tmOpenFromMinsGMT: 00,
					tmClosedFromHourGMT: 23,
					tmClosedFromMinsGMT: 59,
					tmOpenDate: 1,
					tmClosedDate: 1,
					tmOpenMonth: 9, //starts from zero
					tmClosedMonth: 11, //starts from zero
					tmOpenYear: 2012,
					tmClosedYear: 2012,
					tmMaxTweets: 20
				},
	uzbek:	    {   multiClipEmpItems: 3 },
	ukchina_simplified: { empFontSupported: false, empHighlightColour: '0xE86C00'},
	ukchina_traditional: { empFontSupported: false, empHighlightColour: '0xE86C00'},
	urdu:       {   
					sampleText:'بی بی سی دیگر سائٹوں پر شائع شدہ مواد کی ذمہ دار نہیں ہے',
					empFontSupported: false
				},
	vietnamese:	     {   multiClipEmpItems: 3 },
	worldservice:	     { },
	chinese_simplified: 	{	empFontSupported: false },
	chinese_traditional: 	{	empFontSupported: false },
	cojo_gel:	{}
}


ws.selectors = {
    // Selectors used for unobtrusive JS replacement
    boxQuote: '.bx-quote',
    browserBack: '.ws-back',
    businessFeed: '.bx-businessfeed',
    carousel: '.li-carousel',    
    collapsedList: '.li-collapsed',    
    definitionList: '.li-definition',
    definitionAv: '.li-avdefinition',
    emp: '.emp, .cEMP',
    enlargeImage: '.bx-enlargeimage',                  
    fontCheck: '.font-check',
    scrollable: '.scrollable',
    pictureGallery: '.li-picturegallery',
    liveText: '#live-text',
    liveEvent: '.live-event',
    liveEventLiveStatus: '.live-event.live',
    liveMAPTeaser: '.ts-av-live',
    liveMAPAsset: '.av-live',
    moreMultimediaTabs: '.li-moremultimedia',
    personalisedList: '.li-personalised',
    printLink: '.document-tools .print a',
	socialBookmarkPanel:'.document-tools',
    scrollingAnchors: '.scrolling-anchors',
    tabbedList: '.li-tabbed',   
    tabbedStory: '.tabs-v, .tabs-h',
    tabbed: '.tabbed',      
    ticker: '.li-ticker',
    timeline: '.li-simpletimeline',
    validateForms: '.validate',
    vote: '.wsv',
    timeAgo: '.date, .timeago',
    multiClipEmp: '.li-multiclipemp',
    staticMap: '.static-map',
	inlineContextualLinks: '.contextual-links',
	topicsAtoZ: '.li-topics',
	servicesNav: '#news-services',
	simpleVerticalAccordion: '.simple-vertical-accordion',
	changeDegreesUnits: '#change-degrees',
    dynamicSSI: '.ssi',
    drawers: '.li-drawers',
    rollingNews: '.bx-rollingnews',
    marketDataFeeds: '.bx-businessfeed',
    slideshowTeaser: '.ts-slideshow',
	tweetMinster: '.bx-tweetminster',
	imageReplace: '.image-replace'
}


ws.init = function(glowLib) {

    glow = glowLib; // Make available globally
    this._onloadFunctionsQueue = function() { ws.isReady = true; };
    this._requiredOnloadFunctions = new Array;
    this._epochOnPageLoad = new Date().getTime();
  
    // Set environment vars
    this.env = {
        userAgent: navigator.userAgent || '',    
        lang: glow.dom.get('html').attr('lang'),
        assetRoot: (location.href.match('www.bbc.co.uk')) ? 'http://wscdn.bbc.co.uk' : '',
        jsRoot:  '/worldservice/scripts/core/2/',
        cssRoot: '/worldservice/styles/core/2/screen/',
	isLive: location.href.match(/^http:\/\/(www|delta|dev\.publish\.topcat\.ws)\.bbc\.co\.uk/) ? true : false,
	isReallyLive: location.href.match(/^http:\/\/(www|delta)\.bbc\.co\.uk/) ? true : false,
        isTC2Live: location.href.match(/topcat\.bbc\.co\.uk/) ? true : false,        
        modules: {},
        empPlaying: 0 // Keeps track of how many EMP players are playing on the page (usually just 1)          
    };            

    this.env.jsRoot = location.href.match(/www\.bbc\.co\.uk/) ? 'http://wscdn.bbc.co.uk'+this.env.jsRoot : this.env.jsRoot;            
        
    glow.ready(function() {
    	ws.env.direction = glow.dom.get('#blq-content').css('direction');    
    
        // Load extra JS files if not loaded already    
        ws.utils.loadModule('modules');      
        ws.utils.loadModule('media');
    
        //glow.dom.get('#blq-content').append('<h2>WS CoreJS '+ws.version+' loaded - Glow '+glow.VERSION+'</h2>');
         
        // Insert div to check when CSS is loaded
        glow.dom.create('<div id="css-ready"></div>').appendTo('body');                            
        
		// If livetext, rollingnews or lastupdated is on the page, periodically
		// check the live config for any changes in refresh intervals, or kill switches
	if (glow.dom.get(ws.selectors.liveEvent+','+ws.selectors.liveText+','+ws.selectors.rollingNews+',.last-published,'+ws.selectors.tweetMinster).length) {
            ws.net.checkLiveConfig();
        }    			        
        
        // Load vocab file
        ws.vocab.loadDictionary();  
		
		// tidy pages
		ws.utils.tidyPages();
		
		// For Chrome/Opera on Macs, add noembed font as ligatures don't load properly
		//if (ws.env.userAgent.match(/Mac/) && ws.env.userAgent.match(/Chrome|Opera/)) { glow.dom.get('html').addClass('ws-noembedfont'); }
        
        // Fire onload events
        ws.utils._fireOnloadEvents();       
		
		// TC2 Preview cleanup		
	    if (!ws.env.isLive) { 
	        ws.utils.loadSSIContent(ws.selectors.dynamicSSI);
            ws.utils.cleanSSIErrors(); 
        }
        
        if (glow.dom.get(ws.selectors.emp+','+ws.selectors.multiClipEmp).length) {
            //var flashVersion = glow.embed.Flash.version().major;	
			var empVersion = ws.config[ws.env.service].empVersion || ws.config.defaultEmpVersion;
			ws.utils.loadJS('http://www.bbc.co.uk/emp/swfobject.js', 'SWFObject');
			//if (ws.env.empVersion == 3 && flashVersion >= 10) {
			if (empVersion == 3) {
				ws.utils.loadJS('http://www.bbc.co.uk/emp/bump?emp=worldwide', 'embeddedMedia');
			} else {			
				ws.utils.loadJS('http://www.bbc.co.uk/emp/embed.js', 'embeddedMedia');
			}
        }        
		
    });
        
    ws.onload(function() {
        // Unobtrusively insert components and modules               
        ws.media.emp(ws.selectors.emp);
        ws.media.multiClipEMP(ws.selectors.multiClipEmp);
        ws.modules.carousel(ws.selectors.carousel);        
        ws.modules.enlargeImage(ws.selectors.enlargeImage);
        ws.modules.pictureGallery(ws.selectors.pictureGallery);
        ws.modules.tabbed(ws.selectors.tabbed);
		ws.modules.tabbedStory(ws.selectors.tabbedStory);
		ws.modules.inlineContextualLinks(ws.selectors.inlineContextualLinks);
        ws.modules.ticker(ws.selectors.ticker);
        ws.modules.moreMultimediaTabs(ws.selectors.moreMultimediaTabs);        
        ws.modules.timeline(ws.selectors.timeline);
        ws.modules.liveText(ws.selectors.liveText);        
        ws.modules.topicsAtoZ(ws.selectors.topicsAtoZ);
        ws.modules.browserBack(ws.selectors.browserBack);
		ws.modules.simpleVerticalAccordion(ws.selectors.simpleVerticalAccordion);
        ws.modules.servicesNav(ws.selectors.servicesNav);
        ws.modules.validateForms(ws.selectors.validateForms);
		ws.modules.changeDegreesUnits(ws.selectors.changeDegreesUnits);   
		ws.modules.drawers(ws.selectors.drawers);
		ws.modules.rollingNews(ws.selectors.rollingNews); 
		ws.modules.marketDataFeeds(ws.selectors.marketDataFeeds);   
		ws.modules.socialBookmarkPanel(ws.selectors.socialBookmarkPanel); 
		ws.modules.slideshowTeaser(ws.selectors.slideshowTeaser); 
		ws.modules.definitionList(ws.selectors.definitionList);
		ws.modules.definitionAv(ws.selectors.definitionAv);
        //glow.events.addListener(ws.selectors.printLink, 'click', function() { window.print(); return false; });



		// end functions
        ws.modules.popup();
		//timeago should be the last function called.
		ws.modules.timeAgo(ws.selectors.timeAgo);  
	ws.modules.liveEventsShare();
		ws.modules.loaded=true;
		
    })
    
    // Load debug module when not live
    if (!ws.env.isLive) { ws.utils.loadModule('debug'); }
	
    // Shortcuts
    ws.console = ws.utils.console;      
}


ws.onload = function(callback) {      
    // Add the function to the main queue, to be fired when everything is loaded
    var oldOnloadFunctions = ws._onloadFunctionsQueue;
    	ws._onloadFunctionsQueue = function() {
    		callback();
    		oldOnloadFunctions();    		
  	};
}

ws.flagpole = {
	flastmod: {},
	init: function() {
		ws.flagpole.className='';
		//livestats
		ws.flagpole.hrs = 6;
		if (ws.flagpole.flastmod.livestats) {
			ws.flagpole.dist = (ws.env.serverDate.getTime()-ws.flagpole.flastmod.livestats.getTime());
			if (ws.flagpole.dist > ws.flagpole.hrs*60*60*1000) { 
				ws.flagpole.className+=' fp-livestats';
			}
		}
		else { ws.flagpole.className+=' fp-livestats'; }
		
		ws.flagpole.hrs = 3;
		if (ws.flagpole.flastmod.commodities) {
			ws.flagpole.dist = (ws.env.serverDate.getTime()-ws.flagpole.flastmod.commodities.getTime());
			if (ws.flagpole.dist > ws.flagpole.hrs*60*60*1000) { 
				ws.flagpole.className+=' fp-commodities';
			}
		}
		else { ws.flagpole.className+=' fp-commodities'; }

		ws.flagpole.hrs = 3;
		if (ws.flagpole.flastmod.currencies) {
			ws.flagpole.dist = (ws.env.serverDate.getTime()-ws.flagpole.flastmod.currencies.getTime());
			if (ws.flagpole.dist > ws.flagpole.hrs*60*60*1000) { 
				ws.flagpole.className+=' fp-currencies';
			}
		}
		else { ws.flagpole.className+=' fp-currencies'; }

		ws.flagpole.hrs = 3;
		if (ws.flagpole.flastmod.markets) {
			ws.flagpole.dist = (ws.env.serverDate.getTime()-ws.flagpole.flastmod.markets.getTime());
			if (ws.flagpole.dist > ws.flagpole.hrs*60*60*1000) { 
				ws.flagpole.className+=' fp-markets';
			}
		}
		else { ws.flagpole.className+=' fp-markets'; }
		
	    if (typeof document.documentElement.className == 'string') {
	        document.documentElement.className += ws.flagpole.className;
	   	} else {
	       	document.documentElement.className = ws.flagpole.className;
	    }
	}
}

ws.utils = {
    _fireOnloadEvents: function() {
        // This will fire the onload events, if all the required dependencies are present
        // It will go through ws._requiredOnloadFunctions(), and if any are 'undefined', it will
        // wait and try again
        var canFireOnloadEvents = true;
        glow.lang.map(ws._requiredOnloadFunctions, function(functionName) {
          var functionType = eval('typeof('+functionName+')');
          if ((functionType) == 'undefined') { canFireOnloadEvents = false; }          
        });
        
        if (glow.dom.get('#css-ready').css('z-index') != '1234') { canFireOnloadEvents = false; }                
        
        if (canFireOnloadEvents) {
          glow.dom.get('#css-ready').remove();
          ws._onloadFunctionsQueue();
        } else {
          setTimeout('ws.utils._fireOnloadEvents()', 50);
        }
    },

    loadJS: function(url, requiredFunctionName) {                                           
            if (eval('typeof '+requiredFunctionName) != 'undefined') return; // Do not attempt to load JS if module is already loaded
        
            if (ws.debug) {
                var cache = false;
              } else {
                var cache = true;
                url += '?'+ws.env.assetsVersion;
            }
    
            glow.net.loadScript(url, { useCache: cache });
            
    		if (typeof(requiredFunctionName) != 'undefined') {
              // This adds a name to the list of functions/global variables that need to be
              // present before ws.onload() functions are fired. This is to make sure that all
              // external scripts have been loaded before proceeding
              ws._requiredOnloadFunctions[ws._requiredOnloadFunctions.length] = requiredFunctionName;
            }
    },
            
    loadModule: function(module) {
        this.loadJS(ws.env.jsRoot+'modules/'+module+'.js', 'ws.'+module);
    },

    loadCSS: function(url) {
        glow.dom.get('head').append('<link href="'+(ws.env.cssRoot+url)+'" rel="stylesheet" type="text/css"/>');
    },

    console: function(msg) {
        // Sends a message to the Firebug console
        if ((typeof console != 'undefined') && (this.debug === true)) { console.log(msg); }
    },
    
    uid: function(prefix) {
        if (typeof(prefix) == 'undefined') { prefix = ''; } else { prefix += '-'; }
        return prefix+Math.floor(Math.random()*10000);
    },
      
    outerHtml: function(selector) {
      var tmpNode = glow.dom.create('<div></div>').append(glow.dom.get(selector).clone());
      var markup = tmpNode.html();  
      tmpNode.destroy();
      return markup;
    },
    
    getSlotWidth: function(selector) {
      var element = glow.dom.get(selector),
          container = element;

      if (element.length > 0) {
        while (!container.hasClass('g-container')) {
          if (container.is('body')) { return false; }
          container = container.parent();          
        }
        var slotWidth = container.width();
        /*
        if (glow.dom.get('.bodytext').length) {
          slotWidth = glow.dom.get('.bodytext').width();
        }*/        
        return slotWidth;
      } else {
        return false;
      }
    },
    
    getParentWithClass: function(elm, className) {
      elm = glow.dom.get(elm).slice(0,1);
      className = className.replace(/\./i, '');
      while ( !elm.hasClass(className) ) {
        elm = elm.parent();
        if (elm[0].nodeName.toLowerCase() == "body") return new glow.dom.NodeList();
      }
      return elm;
    },
	
    cleanSSIErrors: function() {
        var $ = glow.dom.get;
        $('#blq-main div').each(function() {
          var cleaned = $(this).html();
          cleaned = cleaned.replace(/\[an\ error\ occurred\ while\ processing\ this\ directive\]/g, '');
          // Workaround for IE stripping out style tags
          if (glow.env.ie) { cleaned = cleaned.replace(/<style/gi, '<span style="display:none">&nbsp;</span><style'); }
          $(this).html(cleaned);
        });
    },
    
    
    loadSSIContent: function(selector) {
        glow.dom.get(".ssi").each(function() { 
          var currentElement = glow.dom.get(this),
              contentUrl = "http://www.bbc.co.uk/worldservice/includes/core/2/tools/tc2_include_previewer.sssi?href="+currentElement.attr('href')+"&service="+ws.env.service+"&documentType="+ws.env.documentType+"&genre="+ws.env.genre,
              tunnelUrl = "/cgi-bin/topcat2/open/tunnel.pl?";
	        if ( currentElement.html().match('error occurred') || currentElement.html().match('/\(none\)/') ) {
              glow.net.get(tunnelUrl+contentUrl, {
                useCache: true,
                async: false,
                onLoad: function(response) {
					if (!response.text().match("<!DOCTYPE") && !response.text().match("404 Not Found") && !response.text().match("an error occurred while processing this directive") ) {
       	              currentElement.html(response.text());
					}
                }
              });
            }
        });
    },

    getGMTEpoch: function() {
        var msecsSincePageLoad = new Date().getTime() - ws._epochOnPageLoad,
            gmtEpoch = Math.round((ws.env.serverDate.getTime() + msecsSincePageLoad)/1000);
        return gmtEpoch;     
    },
    
	tidyPages: function() {
	
		// HTML5 EMP player - turn off autoplay (do not move from P1)
		glow.dom.get(".emp-html-embed video").each(function() {
			glow.dom.get(this).removeAttr("autoplay");
		});
		glow.dom.get(".emp-html-embed audio").each(function() {
			glow.dom.get(this).removeAttr("autoplay");
		});

		// tidy cta hover for av headline+text teasers - move to tidy function?
		glow.events.addListener(".ts-headline.ts-audio .body a .cta, .ts-headline.ts-video .body a .cta", 'mouseover', function() { 
			var teaser = ws.utils.getParentWithClass(this, 'ts-headline');
			glow.dom.get(this).addClass('hover'); 
			glow.dom.get(teaser).get('.title').css('text-decoration', 'underline'); 
			glow.dom.get(teaser).get('.associated .cta').removeClass('hover'); 
			return false; 
		});
        
		glow.events.addListener(".ts-headline.ts-audio .body a .cta, .ts-headline.ts-video .body a .cta", 'mouseout', function() { 
			var teaser = ws.utils.getParentWithClass(this, 'ts-headline');
			//glow.dom.get(this).removeClass('hover');
			glow.dom.get(teaser).get('.title').css('text-decoration', 'none');
			glow.dom.get(teaser).get('.cta').removeClass('hover');  
			return false; 
		});

		glow.events.addListener(".ts-headline.ts-audio .title a, .ts-headline.ts-video .title a", 'mouseover', function() { 
			var teaser = ws.utils.getParentWithClass(this, 'ts-headline');
			glow.dom.get(teaser).get('.body a .cta').addClass('hover'); 
			glow.dom.get(teaser).get('.associated .cta').removeClass('hover'); 
			return false; 
		});
        
		glow.events.addListener(".ts-headline.ts-audio .title a, .ts-headline.ts-video .title a", 'mouseout', function() { 
			var teaser = ws.utils.getParentWithClass(this, 'ts-headline');
			//glow.dom.get(teaser).get('.body a .cta').removeClass('hover'); 
			glow.dom.get(teaser).get('.cta').removeClass('hover');  
			return false; 
		});
						
		// EMP fixes
		if (glow.dom.get('body').hasClass('genre-videoyfotos') && glow.dom.get('body').hasClass('index')) {
			glow.dom.get('body').addClass('genre-multimedia').removeClass('genre-videoyfotos');
		}
		
		/** Live Events teaser fixes **/
		
		// top-story
		glow.dom.get('.top-story .live-event-promo-teaser').each(function() {
		    var _teaserParent = glow.dom.get(this.parentNode.parentNode);
		    if( _teaserParent.get('img').length > 0 ) {
			var _teaserImage = _teaserParent.get('img')[0];
			this.parentNode.removeChild(this);
			_teaserImage.parentNode.insertBefore(this, _teaserImage);
			var _pos = glow.dom.get(_teaserImage).position();
			glow.dom.get(this).css(_pos);
		  	glow.dom.get(this).show();
			}
		});
		
		if (glow.dom.get(ws.selectors.liveEvent).length) {
			// quick fix to disable ago for archieved live events
			glow.dom.get(".live-event.asithappened .livetext_item .timeago").removeClass("timeago").addClass("archived-datestamp");
			ws.utils.imageICrevert(ws.selectors.imageReplace);
		}

		// weather temporary solution to uniform headers
		if(glow.dom.get('.w4-h1').length && ws.env.service != "somali") {
			glow.dom.get('h1').remove();
			glow.dom.create("<h1 class=\"w4-h1\">"+glow.dom.get('.w4-h1').html()+"</h1>").appendTo('#weather-title');
			glow.dom.get('h2.w4-h1').remove();
		}

		glow.dom.get(ws.selectors.emp).each(function() {
			var node 		= glow.dom.get(this), 
				classname 	= node.attr('class')+' ',
				format 		= classname.match(/emp-f-(.*?)\ /)[1],
				bodyNode 	= glow.dom.get('body');					
		
            // Check if audio EMP should be displayed in standard video mode (eg. Afrique radio progs)
            if (typeof(ws.config[ws.env.service].empStandardDisplayMode) != 'undefined' && format == 'audio') {
                var documents = ws.config[ws.env.service].empStandardDisplayMode.documents || undefined,
                    selectors = ws.config[ws.env.service].empStandardDisplayMode.selectors || undefined;
                for (var i in documents) {
                    if (location.href.match(documents[i])) {
                        node.removeClass('emp-f-audio').addClass('emp-f-video'); 
                        format = 'video'; 
                    }
                }
                if (glow.dom.get(selectors).length) { 
                    format = 'video';
                    node.removeClass('emp-f-audio').addClass('emp-f-video');
                    node.parent().removeClass('ts-audio').addClass('ts-video'); 
                }
            }        
        	
        	// genre multimedia index override
			if (bodyNode.hasClass('index') && bodyNode.hasClass('genre-multimedia') && ws.utils.getParentWithClass(node, 'top-story') && node.parent().hasClass('teaser') && format=='video') { 
				node.parent().removeClass('ts-256emp');
				node.parent().removeClass('ts-512emp');
				node.parent().addClass('ts-640emp');
			}
		});
        
		// special features list

		glow.dom.get(".g-w20 .li-specialfeatures").each(function() {
			
		var currentList = glow.dom.get(this),
			innerList='';

			currentList.get(".teaser").each(function(i) {
				var currentTs = glow.dom.get(this);
				if (i>0) {
					innerList+=ws.utils.outerHtml(currentTs);
					currentTs.destroy();
				}
			});
			
			if(innerList!=''){
				currentList.get(".body").append('<ul class="inner-list">'+innerList+'</ul>');	
			}		
		});
		
		// adding class to special features emp teaser
		glow.dom.get(".g-w11 .li-specialfeatures").each(function() {
			var currentElement = glow.dom.get(this);
				currentElement.get(".ts-256emp.ts-video.teaser > a").each(function(i) {
				glow.dom.get(this.parentNode).addClass('no-body');
			});
		});
		
		// move the timeago element to inside the summary
		
		glow.dom.get(".last-published .teaser .timeago").each(function() {
			
			var timeagoItem = glow.dom.get(this),
				parentTeaser = ws.utils.getParentWithClass(this, 'teaser');
			
			if (parentTeaser.get('.body .summary').length > 0) {
				// if theres a summary insert timeago as a span inside the end of the summary and leave the intitial empty space.
				var newTimeagoItem = ' <span id="' + timeagoItem.attr('id') + '" class="' + timeagoItem.attr('class') + '" style="">' + timeagoItem.text() + '</span>';												
				parentTeaser.get('.body .summary').append(newTimeagoItem);
				timeagoItem.destroy();								
			} else if (parentTeaser.get('.title').length > 0){
				// if theres no summary add it directly after the title
				parentTeaser.get('.title').after(timeagoItem);
			}						
		});
		
		
		// JS to remove backslashes from send-to-friend page title - special chars in the querystring are sometimes preceeded with backslashes
		// and its been difficult to remove them with ssi regex :(		
		
		glow.dom.get('body#send-to-friend h2 span').each(function() {
			var formtitle = glow.dom.get(this).text();
			glow.dom.get(this).text(formtitle.replace(/\\/g,''));			
		});
		
		// remove empty/broken teasers from li-moremultimedia
		glow.dom.get(".li-moremultimedia").each(function() {
			var currentList = glow.dom.get(this);
			currentList.get(".teaser").each(function(i) {
				var currentTs = glow.dom.get(this);
				if (currentTs.get("img").length && currentTs.get("img").attr("src").match("(none)")) {
					currentTs.destroy();
				}
			});
		});		
		
		glow.dom.get('.bx-livestats .body ol li a').each(function() {		
			var lsLink=glow.dom.get(this).attr('href'),	
			documentPath=lsLink.split(ws.env.servicePath),
			newPath="http://www.bbc.co.uk"+ws.env.servicePath+documentPath[1];
			glow.dom.get(this).attr("href", newPath);
		});
	},
	//reverts ICed img src to its original size
	imageICrevert : function(selector) {
        	var _recipeToSrip = /ic\/\d+x\d+\/worldservice\//g;
       		glow.dom.get(selector).each(function(){
            		var current = this;
            		var current_src = current.getAttribute('src');
            		if (current_src.search(_recipeToSrip) != -1) {
                		original_src = current_src.replace(_recipeToSrip , "" );
                		current.setAttribute('src',original_src);
            		}
        	});
    	},    
	truncate : function(str, maxLength, suffix)	{
    		if(str.length > maxLength) {
        		str = str.substring(0, maxLength + 1); 
        		str = str.substring(0, Math.min(str.length, str.lastIndexOf(" ")));
        		str = str + suffix;
    		}
    		return str;
	},
 	setCookie : function(name,value,days) {
		if (days) {
			var date = new Date();
			date.setTime(date.getTime()+(days*24*60*60*1000));
			var expires = "; expires="+date.toGMTString();
		}
		else var expires = "";
		document.cookie = name+"="+value+expires+"; path=/";
	},

 	setCookieMinutes : function(name,value,minutes) {
		if (minutes) {
			var date = new Date();
			date.setTime(date.getTime()+(minutes*60*1000));
			var expires = "; expires="+date.toGMTString();
		}
		else var expires = "";
		document.cookie = name+"="+value+expires+"; path=/";
	},

	readCookie : function(name) {
		var nameEQ = name + "=";
		var ca = document.cookie.split(';');
		for(var i=0;i < ca.length;i++) {
			var c = ca[i];
			while (c.charAt(0)==' ') c = c.substring(1,c.length);
			if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
		}
		return null;
	}			

} 

/* Vocab */
ws.vocab = {                             
    dictionaryLoaded: false,
    
    // Retrieval method
    get: function(term) {
      // Load dictionary for the current service
      if (ws.vocab.dictionaryLoaded == false) {
         ws.loadJS(ws.jsRoot+'vocab/'+ws.currentService+'.js', 'ws.vocab.dictionary');  
         ws.vocab.dictionaryLoaded = true;
      }
      return ws.vocab.dictionary[term];          
    },
    
    loadDictionary: function() {
    	ws.utils.loadJS(ws.env.jsRoot+'vocab/'+ws.env.lang+'.js', 'ws.vocab.dictionary');        
        //ws.loadJS(ws.jsRoot+'vocab/'+ws.env.service+'.js', 'ws.vocab.dictionary');
        ws.vocab.dictionaryLoaded = true;
    }		
};


ws.net = {
    checkLiveConfig: function() {
	glow.net.post('/worldservice/scripts/core/config.json', '',{
            useCache: true,
            async: false,
            onLoad: function(response) {
                response = response.json();
                if (!ws.env.liveText) { ws.env.liveText = {} }
                ws.env.liveText.active = response.livetext.enabled;
                ws.env.liveText.refreshInterval = parseInt(response.livetext.refreshInSecs) * 1000;
                
                if (!ws.env.lastPublished) { ws.env.lastPublished = {} }                
                ws.env.lastPublished.active = response.last_published.enabled;
                ws.env.lastPublished.refreshInterval = parseInt(response.last_published.refreshInSecs) * 1000;
                
                if (!ws.env.rollingNews) { ws.env.rollingNews = {} }                
                ws.env.rollingNews.active = response.rolling_news.enabled;
                ws.env.rollingNews.refreshInterval = parseInt(response.rolling_news.refreshInSecs) * 1000;   

				if (!ws.env.tweetMinster) { ws.env.tweetMinster = {} }                
                ws.env.tweetMinster.active = response.tweet_minster.enabled;
                ws.env.tweetMinster.refreshInterval = parseInt(response.tweet_minster.refreshInSecs) * 1000; 
				ws.env.tweetMinster.openTime = response.tweet_minster.openingTime;
				ws.env.tweetMinster.closeTime = response.tweet_minster.closingTime;	
				ws.env.tweetMinster.refreshStatuses = parseInt(response.tweet_minster.refreshInSecsStatuses) * 1000; 
				ws.env.tweetMinster.refreshStories = parseInt(response.tweet_minster.refreshInSecsStories) * 1000; 
				ws.env.tweetMinster.refreshKeywords = parseInt(response.tweet_minster.refreshInSecsKeywords) * 1000; 
				ws.env.tweetMinster.refreshActive = parseInt(response.tweet_minster.refreshInSecsActive) * 1000; 
				//ws.env.tweetMinster.tmHandle = [];
		
		
		if (!ws.env.live_events) { ws.env.live_events = {} }                
                ws.env.live_events.enabled = response.live_events.enabled;
                ws.env.live_events.refreshInterval = response.live_events.refreshRateInSeconds;
		ws.env.live_events.itemsPerRequest = parseInt(response.live_events.itemsPerRequest); 
	    }
	});
        
        setTimeout(ws.net.checkLiveConfig, ws.config.liveConfigRefreshInterval);
    }
}


ws.events = {
	/* Functions called by swf to provide event interactions eg AV Glossary in UKChina */
	/* mp3PlayerReady called when the swf is loaded */
	/* embedID is set by glow embed function as flashvars, */ 
	/* then picked up by swf and fed back so these functions can be reused with any swf */
	mp3PlayerReady: function(embedID) {
		//alert('enable');
		glow.events.fire('#'+ embedID, 'ready');		
	},
	/* mp3PlayerAudioFinished called when the mp3 file has finished playing */
	mp3PlayerAudioFinished: function(embedID) {
		//alert("finished");
		glow.events.fire('#'+ embedID, 'finished');		
	}
}
    
  
/* Put IE6 classname as soon as possible */
if (navigator.userAgent.toLowerCase().indexOf('msie 6') != -1) {
    var docElement = document.documentElement;
    if (typeof docElement.className == 'string') {
        docElement.className += ' ie6';
    } else {
        docElement.className = 'ie6';
    }
}
  
/* Load Glow */
gloader.load([  'glow', ws.glowVersion,
                'glow.dom',
                'glow.data',
                'glow.forms',
                'glow.net',
                'glow.i18n',
                'glow.embed',
                'glow.events',
                'glow.dragdrop',
                'glow.widgets.Carousel',
                'glow.widgets.Overlay',
                'glow.widgets.InfoPanel',
                'glow.widgets.Panel',
                'glow.widgets.Slider'
        ], {
        onLoad: function(glow) { ws.init(glow); }
    }
);  







/***************************************************************************************************
*  	Prototype functions
*
*	This section is for any core JS changes using prototype.
*		- Changes under this section will a potentially HUGE impact and should
*		only be added with extreme care!
***************************************************************************************************/




/*
*	Bind - 	allows the binding of a function to the 'this' keyword to ensure that the scope within the
*		function is maintained. (e.g. HTMLNode.click = function() { this.a = 1; }.bind(this); )
*
*	Code block taken from: https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Function/bind
*/
if (!Function.prototype.bind) {  
      Function.prototype.bind = function (oThis) {  
        if (typeof this !== "function") {  
          // closest thing possible to the ECMAScript 5 internal IsCallable function  
          throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");  
        }  
      
        var aArgs = Array.prototype.slice.call(arguments, 1),   
            fToBind = this,   
            fNOP = function () {},  
            fBound = function () {  
              return fToBind.apply(this instanceof fNOP  
                                     ? this  
                                     : oThis || window,  
                                   aArgs.concat(Array.prototype.slice.call(arguments)));  
            };  
      
        fNOP.prototype = this.prototype;  
        fBound.prototype = new fNOP();  
      
        return fBound;  
    };  
}  
