
  //var estado = '[{"value": 1, "text": "AC", "continent": "Task"}, {"value": 2, "text": "AL", "continent": "Task"}, {"value": 3, "text": "AM", "continent": "Task"}, {"value": 4, "text": "AP", "continent": "Task"}, {"value": 5, "text": "BA", "continent": "Task"}, {"value": 6, "text": "CE", "continent": "Task"}, {"value": 7, "text": "DF", "continent": "Task"}, {"value": 8, "text": "ES", "continent": "Task"}, {"value": 9, "text": "GO", "continent": "Task"}, {"value": 10, "text": "MA", "continent": "Task"}, {"value": 11, "text": "MG", "continent": "Task"}, {"value": 12, "text": "MS", "continent": "Task"}, {"value": 13, "text": "MT", "continent": "Task"}, {"value": 14, "text": "PA", "continent": "Task"}, {"value": 15, "text": "PB", "continent": "Task"}, {"value": 16, "text": "PE", "continent": "Task"}, {"value": 17, "text": "PI", "continent": "Task"}, {"value": 18, "text": "PR", "continent": "Task"}, {"value": 19, "text": "RJ", "continent": "Task"}, {"value": 20, "text": "RN", "continent": "Task"}, {"value": 21, "text": "RO", "continent": "Task"}, {"value": 22, "text": "RR", "continent": "Task"}, {"value": 23, "text": "RS", "continent": "Task"}, {"value": 24, "text": "SC", "continent": "Task"}, {"value": 25, "text": "SE", "continent": "Task"}, {"value": 26, "text": "SP", "continent": "Task"}, {"value": 27, "text": "TO", "continent": "Task"}]';
  var estados_ori = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'TODOS'];
  var mercados_ori = ['Advertising', 'S/N', 'Vendas e Marketing', 'Recursos Humanos', 'Meio Ambiente', 'Indústria', 'Internet', 'Transportes', 'Energia', 'Seguros', 'Infantil', 'Direito', 'Automobilismo', 'Educação', 'E-commerce', 'Gestão', 'Saúde e Bem-estar', 'Produtos de Consumo', 'Cloud Computing', 'Outros', 'Mobile', 'Games', 'TIC e Telecom', 'Logística e Mobilidade Urbana', 'Desenvolvimento de Software', 'Hardware', 'Imobiliário', 'Biotecnologia', 'Finanças', 'Varejo / Atacado', 'Esportes', 'Comunicação e Mídia', 'Agronegócio', 'Serviços Profissionais', 'CRM', 'Nanotecnologia', 'Big Data', 'Pets', 'Construção Civil', 'Segurança e Defesa', 'Casa e Família', 'Entretenimento', 'Eventos e Turismo', 'Moda e Beleza', 'Recrutamento', 'Video'];
  var stacks_ori = ['.NET', '.NET 4.5', '.NET Core', '.NET MVC', '4D', 'ABAP', 'Ably Realtime', 'ABNF', 'ACDSee', 'Ada', 'Administrador de sistema', 'Adobe Air', 'Adobe Flash', 'Adobe Flash Builder', 'Adobe Flex', 'Adobe PhoneGap', 'AdonisJS', 'ADVPL', 'ADVPL ASP', 'Agavi', 'Agda', 'AgilePHP', 'AGS Script', 'Ajax', 'AlertOps', 'Algolia', 'Alloy', 'Amazon API Gateway', 'Amazon AppStream', 'Amazon Aurora', 'Amazon DynamoDB', 'Amazon ElastiCache', 'Amazon Elasticsearch Service', 'Amazon RDS for MariaDB', 'Amazon RDS for MySQL', 'Amazon Rekognition', 'Amazon Relational Database Service (RDS)', 'Amazon Simple Notification Service (SNS)', 'Amazon Simple Workflow Service (SWF)', 'Amazon SimpleDB', 'amCharts', 'AMP', 'Android', 'Android Studio', 'Angular', 'Angularjs', 'ANTLR', 'Apache', 'Apache ActiveMQ', 'Apache Cassandra', 'Apache Cocoon', 'Apache Commons', 'Apache Cordova', 'Apache Drill', 'Apache Giraph', 'Apache Groovy', 'Apache HAWQ', 'Apache Impala', 'Apache jclouds', 'Apache Jena', 'Apache Kafka', 'Apache NetBeans', 'Apache Nutch', 'Apache Phoenix', 'Apache POI', 'Apache Qpid', 'Apache Sling', 'Apache Solr', 'Apache Struts', 'Apache Tika', 'Apache Tiles', 'Apache Wicket', 'Apex', 'API', 'Appbot', 'Apple Safari', 'AppleScript', 'ArcGIS', 'ArcGIS Online', 'ArcGIS Pro', 'Arduino', 'ARKit', 'ASN.1', 'ASP', 'ASP.NET', 'ASP.NET Core', 'ASP.NET MVC', 'Assembly', 'Atom', 'Aura', 'AWS Amplify', 'AWS Chatbot', 'AWS Cloud9', 'AWS EC2 (Elastic Compute Cloud)', 'AWS Mobile Services', 'AWS RDS (Relational Database Service)', 'AWS S3', 'AWS Step Functions', 'AWS Transit Gateway', 'AWS Trusted Advisor', 'Azure', 'Azure API Management', 'Azure Arc', 'Azure Cognitive Services', 'Azure Computer Vision', 'Azure HDInsight', 'Azure Redis Cache', 'Azure Stack', 'Azure Stack HCI', 'Azure Web Apps', 'Back4App', 'Backbone.js', 'Backendless', 'Bandwidth', 'Bash', 'Beamer', 'Big Data', 'Bing Maps', 'BizTalk Server', 'BizTalk Server 2009', 'BizTalk Server 2010', 'BizTalk Server 2013', 'BizTalk Server 2013 R2', 'BizTalk Server 2016', 'Blade', 'Blockchain', 'Bootstrap', 'Browser Update', 'Bulma', 'C', 'C#', 'C++', 'CA IDMS', 'CA InterTest', 'CakePHP', 'Celery Project', 'CGI::Application', 'Chartbeat', 'Chrome', 'Clean', 'Clean Code', 'Clojure', 'Cloud', 'CloudAMQP', 'CMake', 'COBOL', 'CocoaPods', 'Cocos2d-X', 'CodeIgniter', 'CoffeeScript', 'Cognitect', 'ColdFusion', 'ColdFusion CFC', 'Common Lisp', 'Component Pascal', 'Composer', 'Continuous Delivery', 'Continuous Integration', 'Cordova', 'Couchbase', 'CouchDB', 'CreateJS', 'Crystal', 'CSS', 'CSV', 'Cucumber', 'Cuda', 'Cycript', 'Cypress.io', 'D', 'D2C.io', 'Dart', 'Dassault Systemes', 'Data science', 'DataStax', 'DataTables', 'Datawrapper', 'DB2', 'Dell Boomi', 'Delphi', 'Design Pattern', 'desktop', 'DevOps', 'DIGITAL Command Language', 'Discord', 'Django', 'DM', 'DNS Zone', 'Docker', 'Dockerfile', 'Doctrine', 'Dogescript', 'Dojo', 'Domino 8', 'Drupal', 'Duet Enterprise', 'DynamoDB', 'Dynatrace', 'eC', 'ECLiPSe', 'Eclipse AspectJ', 'Eclipse Jetty', 'ECMAScript', 'egghead.io', 'EJB', 'EJS', 'Elastic Cloud', 'Elasticsearch', 'Elfsight', 'Elixir', 'Ember.js', 'EmberJS', 'Entity framework', 'ERP', 'ES6', 'Estimote', 'Excel', 'Express', 'eXtreme Programming', 'F#', 'Facebook SDK', 'Feathers', 'Fiddler', 'Figma', 'FileMaker', 'FileZilla', 'Firebase', 'Firebird', 'Firebug', 'Flask', 'Flex', 'FlexSlider', 'Flickr API', 'Flot', 'Flutter', 'FLUX', 'Font Awesome', 'Forth', 'Foundation', 'FreeMarker', 'Froala Editor', 'FuelPHP', 'Funnel', 'Game Maker Language', 'GameMaker', 'GDScript', 'Git', 'GLSL', 'Glyphicons', 'Go', 'Google Analytics', 'Google Charts', 'Google Cloud', 'Google Cloud Apigee', 'Google Cloud APIs', 'Google Cloud Bigtable', 'Google Cloud Datastore', 'Google Cloud Endpoints', 'Google Cloud Firestore', 'Google Cloud Messaging', 'Google Cloud SDK', 'Google Cloud Search', 'Google Cloud Spanner', 'Google Cloud Vision API', 'Google Custom Search', 'Google Dialogflow', 'Google Gaming', 'Google Go Language', 'Google Maps Platform', 'Google Search Appliance', 'Google Web Designer', 'Google Web Toolkit', 'GoPlay (Formerly Smartpixel)', 'Gradle', 'Grails', 'Grammatical Framework', 'GraphQL', 'Gravatar', 'Groovy', 'Gulp', 'Gulpjs', 'GWT', 'Halcyon', 'Hanami', 'Handlebars', 'Hazelcast', 'Heroku', 'Hibernate', 'Highcharts', 'HLSL', 'Horde', 'Hornetq', 'Hortonworks', 'HTML', 'HTTP', 'Hugo', 'HybridJava', 'Hybris', 'HydraMVC', 'IAR Embedded Workbench', 'IBM API Connect', 'IBM Cloud Paks', 'IBM Cloud Private', 'IBM HTTP Server', 'IBM ILOG', 'IBM Informix', 'IBM Lotus', 'IBM MobileFirst', 'IBM MQ', 'IBM Rational ClearQuest', 'IBM Rational Rose', 'IBM Sterling Control Center', 'IBM Sterling File Gateway', 'IBM VTAM', 'IBM Watson Discovery', 'IBM Watson Explorer', 'InfluxData', 'Infogram', 'IntelliJ IDEA', 'ionCube PHP Encoder', 'Ionic', 'iOS', 'Ireport', 'Jade', 'Jasmin', 'Jasper', 'Java', 'Java Server Pages', 'JavaEE', 'JavaScript', 'JavaScriptMVC', 'JBoss', 'JBoss Enterprise Web Server (EWS)', 'JCL', 'Jekyll', 'Jenkins', 'Jest', 'JFlex', 'Jitpack', 'jqPlot', 'jQuery', 'JQuery UI', 'JS Bin', 'JSF', 'JSON', 'JSX', 'JUnit', 'Jupyter Notebook', 'K2', 'Kanban', 'Kite', 'Knockout', 'Koa', 'Kohana', 'Kore.ai', 'Kotlin', 'kubernetes', 'Kubernetes-native', 'LabVIEW', 'Laravel', 'Layer7', 'Layer7 API Management', 'Lean', 'Less', 'LibGDX', 'LightBox', 'LightWidget', 'Linux', 'Linux Kernel Module', 'Liquibase', 'Liquid', 'list.js', 'Lodash', 'Logos', 'Lua', 'LUMEN', 'Machine learning', 'Magento', 'MariaDB', 'Material Design Lite', 'Materialize', 'Materialize CSS', 'Mathematica', 'MathJax', 'Matlab', 'Maven POM', 'MemSQL', 'Meteor', 'Micronaut', 'Microsoft Azure', 'Microsoft Azure App Service', 'Microsoft Azure Automation Account', 'Microsoft Azure Bot Service', 'Microsoft Azure Front Door', 'Microsoft Azure Maps', 'Microsoft Azure Spring Cloud', 'Microsoft Bing', 'Microsoft DirectX', 'Microsoft FAST ESP', 'Microsoft Hyper-V Server', 'Microsoft Intune', 'Microsoft Team Foundation Server', 'Microsoft TypeScript', 'Microsoft Virtual Server', 'Microsoft Visual Basic', 'Microsoft Visual FoxPro', 'Microsoft Visual Studio', 'Microsoft.NET', 'Modernizr', 'Module Management System', 'Moment Timezone', 'Moment.js', 'MongoDB', 'Monkey', 'Mootools', 'Mozilla Firefox', 'MQL5', 'MVC', 'MVVM', 'MySQL', 'Nazar', 'NetLinx', 'NextJS', 'Nginx', 'Node.js', 'NodeJS', 'NonStop SQL', 'NoSQL', 'Notepad++', 'NPM', 'NSQ', 'NumPy', 'Objective-C', 'Objective-C++', 'Objective-J', 'OBS', 'Odoo', 'Omgrofl', 'OnBarcode', 'OnGraph', 'OnPage', 'Opa', 'Open JDK HotSpot', 'OpenCL', 'OpenCV', 'Openlayers', 'OpenSSL', 'ORACLE', 'Oracle 11i', 'Oracle ADF Faces', 'Oracle API Gateway', 'Oracle API Manager', 'Oracle API Platform', 'Oracle Database', 'Oracle Fusion Middleware', 'OWl Carousel', 'Pandas', 'Parse', 'Pascal', 'Perl', 'Phabricator', 'Phalcon', 'Phaser', 'Phoenix', 'PhoneGap', 'Photoshop', 'PHP', 'PhpStorm', 'PHPUnit', 'pip python', 'Pivotal tc Server', 'Play', 'PLSQL', 'Pod', 'Polyfill', 'Polymer', 'POO', 'PostgreSQL', 'Postman', 'PostScript', 'PowerBuilder', 'PowerShell', 'POWr', 'pre-commit', 'Prebid', 'Prebid.js', 'Processing', 'Progress', 'Protocol Buffer', 'Prototype', 'Puppet', 'Pure', 'Pure CSS', 'PureMVC', 'PWA', 'PyCharm', 'Pyramid', 'PyTest', 'Python', 'PyTorch', 'QA - Quality Assurance', 'Qlikview', 'QML', 'Qualys Web Application Scanning', 'Quarkus', 'Quartz Scheduler', 'Quasar', 'R', 'RabbitMQ', 'Ragel in Ruby Host', 'RAML', 'RawGit', 'React', 'React Native', 'ReactiveX', 'ReactJS', 'REALbasic', 'Realtime Framework', 'Redis', 'Redux', 'RenderScript', 'RequireJS', 'RESTful', 'RestfulX', 'Retool', 'Riot.js', 'RobotFramework', 'RPM Spec', 'RStudio', 'Ruby', 'Ruby on Rails', 'Rust', 'S.O.L.I.D', 'Sails.js', 'Salesforce', 'Salesforce Lightning Web Components', 'Salesforce Maps', 'SAP', 'SAP HANA', 'SAS', 'SAS Base', 'Sass', 'Scala', 'Scandit', 'Scikit-learn', 'SCORM', 'Script.Aculo.us', 'SCRUM', 'SCSS', 'Select2', 'Selenium', 'Semantic.ui', 'SEO', 'Server', 'Serverless', 'Service Virtualization', 'Sharepoint', 'Shell', 'Shell Script', 'Sinatra', 'Slim', 'Smarty', 'Snap', 'SnapWidget', 'Socket.io', 'Solace', 'Spring', 'Spring Boot', 'Spring Cloud', 'Spring Framework', 'Spring MVC', 'SQF', 'SQL', 'SQL Server', 'SQLite', 'SQLPL', 'StarUML', 'Stencyl', 'Stripes', 'Struts', 'Styled-Components', 'Sublime Text', 'SuperCollider', 'SVG', 'Swift', 'Swiftlet', 'Symfony', 'Syncro', 'T-SQL', 'Tachyons', 'TDD', 'TensorFlow', 'Terra', 'Testes automatizados', 'Testes de Regressão', 'Testes Funcionais', 'Testes unitários', 'The Jupyter Notebook', 'three.js', 'Thymeleaf', 'TI Program', 'TIBCO ActiveSpaces', 'TIBCO FTL', 'TIBCO Managed File Transfer', 'TIBCO Mashery', 'TickCounter', 'TinyMCE', 'Tomcat', 'Tornado', 'TweenMax', 'Twig', 'Typekit', 'TypeScript', 'UIkit', 'UML', 'Underscore.js', 'Unity', 'Unity3D Asset', 'Unix', 'Unreal Engine', 'UnrealScript', 'Vaadin', 'Valve', 'Vanilla', 'VB .NET', 'VB.NET', 'VBA', 'VCL', 'Vercel', 'Vert.x', 'Vertx', 'VictorOps', 'Video.js', 'Vim', 'vis.js', 'Visual Basic', 'Visual Basic.NET', 'Visual Studio Code', 'VMware Tanzu GemFire', 'VTEX', 'Vue.js', 'Web API', 'Web Services', 'web2py', 'webMethods API Gateway', 'Webtask', 'Weeby.co', 'WooCommerce', 'WordPress', 'WPF', 'Xamarin', 'XC', 'Xcode', 'XML', 'XQuery', 'XSLT', 'Yii', 'Zend', 'Zepto', 'Zepto.js', 'Zope'];
  var n_element = 0;
  var connectors = ['AND', 'OR'];
  var not = ['NOT'];

  var estados = [...estados_ori];
  estados.push(...not);
  var mercados = [...mercados_ori];
  var stacks = [...stacks_ori];

  var show_estados = [...estados];
  
  var estados_execute = []
  var mercados_execute = []
  var stacks_execute = []

  function create_button(field)
  {
    if (field == "txt_estados")
    {
        if ($('#txt_estados').val() != 'TODOS') {
          estados_execute.push($('#txt_estados').val());
        }
        teste = "<input type='button' id='e-selecionados_"+n_element+"' class='selecionados' value='"+$('#txt_estados').val()+"'  />"
        n_element ++;
        //const index1 = estados.indexOf($('#txt_estados').val());
        if (connectors.indexOf($('#txt_estados').val()) > -1) {
          console.log("blablalabal");
          i = 0;
          while (show_estados.length > 0) {
            show_estados.splice(0, 1);
          }
          show_estados.push(...estados);
        }
        else if ($('#txt_estados').val() != "" && $('#txt_estados').val() !=  "NOT") {
          const index = estados.indexOf($('#txt_estados').val());
          if (index > -1) {
            estados.splice(index, 1);
          }
          i = 0;
          while (show_estados.length > 0) {
            show_estados.splice(0, 1);
          }
          show_estados.push(...connectors);
        }
        $('#estado-selecionado').append(teste);
        $('#txt_estados').val("");
        $('#txt_estados').focus();
    }

    if (field == "txt_mercados")
    {
        mercados_execute.push($('#txt_mercados').val());
        teste = "<input type='button' id='m-selecionados_"+n_element+"' class='selecionados' value='"+$('#txt_mercados').val()+"' />"
        n_element++
        if ($('#txt_mercados').val() != "") {
          const index = mercados.indexOf($('#txt_mercados').val());
          if (index > -1) {
            mercados.splice(index, 1);
          }
          $('#mercado-selecionado').append(teste);
        }
        $('#txt_mercados').val("");
        $('#txt_mercados').focus();
    }

    if (field == "txt_stacks")
    {
        stacks_execute.push($('#txt_stacks').val());
        teste = "<input type='button' id='s-selecionados_"+n_element+"' class='selecionados' value='" + $('#txt_stacks').val() + "' />"
        n_element++
        if ($('#txt_stacks').val() != "") {
          const index = stacks.indexOf($('#txt_stacks').val());
          if (index > -1) {
            stacks.splice(index, 1);
          }
          $('#stack-selecionado').append(teste);
        }
        $('#txt_stacks').val("");
        $('#txt_stacks').focus();
    }
  }
  
  var teste1 = "mercado_teste";
  var teste2 = "stack_teste";
  var teste3 = "state_teste";


  $(document).ready(function() {

      autocomplete(document.getElementById("txt_estados"), show_estados, 'estado');
      autocomplete(document.getElementById("txt_mercados"), mercados, 'mercado');
      autocomplete(document.getElementById("txt_stacks"), stacks, 'stack');

      $('#submit').click(function() {
        if (mercados_execute.length == 0 && estados_execute.length == 0 && stacks_execute.length == 0)
          alert("Preencher algo");
        else
          window.location.assign("/search?market="+mercados_execute+"&stack="+stacks_execute+"&state="+estados_execute+"&file_name="+$('#file_name').val());
      });
      $('#add_estado').click(function() {
        if ($("#txt_estados").val() === "TODOS"){
          while (estados_execute.length > 0) {
            console.log(estados_execute[0]);
            $("#estado-selecionado").find('[value="'+estados_execute[0]+'"]').remove();
            if (estados_ori.includes(estados_execute[0])) {
              estados.push(estados_execute[0]);
              estados.sort();
              // autocomplete(document.getElementById("txt_estados"), estados);
            }
            const index = estados_execute.indexOf(estados_execute[0]);
            if (index > -1) {
              estados_execute.splice(index, 1);
            }
          }
          $('#txt_estados').val("");
          //autocomplete(document.getElementById("txt_estados"), estados, "estado");
        }
        else if ($("#estado-selecionado").find('[value="TODOS"]').length > 0) {
          console.log("teste");
          console.log($("#estado-selecionado"))
          $("#estado-selecionado").find('[value="TODOS"]').remove();
          estados.push("TODOS");
          estados.sort();
          //autocomplete(document.getElementById("txt_estados"), estados, "estado");
          const index = estados_execute.indexOf("TODOS");
          if (index > -1)
            estados_execute.splice(index, 1);
          create_button("txt_estados");
        }
        else
          create_button("txt_estados");
      });
      $("#estado-selecionado").on('click','',  event =>{
        const clickedElement = $(event.target);
        console.log(event.target.id)
        //console.log(clickedElement.attr('value'));
        $("#estado-selecionado").find('[id="'+clickedElement.attr('id')+'"]').remove();
        if (estados_ori.includes(clickedElement.attr('value'))) {
          estados.push(clickedElement.attr('value'));
          estados.sort();
          //autocomplete(document.getElementById("txt_estados"), estados, "estado");
        }
        if (connectors.indexOf(clickedElement.attr('value')) > -1) {
          i = 0;
          while (show_estados.length > 0) {
            show_estados.splice(0, 1);
          }
          show_estados.push(...connectors);
        }
        else if (clickedElement.attr('value') != 'NOT') {
          i = 0;
          while (show_estados.length > 0) {
            show_estados.splice(0, 1);
          }
          show_estados.push(...estados);
        }
        const index = estados_execute.indexOf(clickedElement.attr('value'));
        //console.log(index)
        if (index > -1) {
          estados_execute.splice(index, 1);
        }
      });
  
      $('#add_mercado').click(function() {
        create_button("txt_mercados");
      });
      $("#mercado-selecionado").on('click','',  event =>{
        const clickedElement = $(event.target);
        //console.log(clickedElement.attr('value'));
        $("#mercado-selecionado").find('[value="'+clickedElement.attr('value')+'"]').remove();
        if (mercados_ori.includes(clickedElement.attr('value'))) {
          mercados.push(clickedElement.attr('value'));
          mercados.sort();
          //autocomplete(document.getElementById("txt_mercados"), mercados, "mercado");
        }

        const index = mercados_execute.indexOf(clickedElement.attr('value'));
        if (index > -1) {
          mercados_execute.splice(index, 1);
        }
      });

      $('#add_stack').click(function () {
        create_button("txt_stacks");
      });
      $("#stack-selecionado").on('click', '', event => {
        const clickedElement = $(event.target);
        //console.log(clickedElement.attr('value'));
        $("#stack-selecionado").find('[value="' + clickedElement.attr('value') + '"]').remove();
        if (stacks_ori.includes(clickedElement.attr('value'))) {
          stacks.push(clickedElement.attr('value'));
          stacks.sort();
          //autocomplete(document.getElementById("txt_stacks"), stacks, "stack");
        }
        //$("#txt_stacks").find('[value="' + clickedElement.attr('value') + '"]').remove();
        const index = stacks_execute.indexOf(clickedElement.attr('value'));
        if (index > -1) {
          stacks_execute.splice(index, 1);
        }
      });
  })
  

  
  //var estado = '[{"value": 1, "text": "AC", "continent": "Task"}, {"value": 2, "text": "AL", "continent": "Task"}, {"value": 3, "text": "AM", "continent": "Task"}, {"value": 4, "text": "AP", "continent": "Task"}, {"value": 5, "text": "BA", "continent": "Task"}, {"value": 6, "text": "CE", "continent": "Task"}, {"value": 7, "text": "DF", "continent": "Task"}, {"value": 8, "text": "ES", "continent": "Task"}, {"value": 9, "text": "GO", "continent": "Task"}, {"value": 10, "text": "MA", "continent": "Task"}, {"value": 11, "text": "MG", "continent": "Task"}, {"value": 12, "text": "MS", "continent": "Task"}, {"value": 13, "text": "MT", "continent": "Task"}, {"value": 14, "text": "PA", "continent": "Task"}, {"value": 15, "text": "PB", "continent": "Task"}, {"value": 16, "text": "PE", "continent": "Task"}, {"value": 17, "text": "PI", "continent": "Task"}, {"value": 18, "text": "PR", "continent": "Task"}, {"value": 19, "text": "RJ", "continent": "Task"}, {"value": 20, "text": "RN", "continent": "Task"}, {"value": 21, "text": "RO", "continent": "Task"}, {"value": 22, "text": "RR", "continent": "Task"}, {"value": 23, "text": "RS", "continent": "Task"}, {"value": 24, "text": "SC", "continent": "Task"}, {"value": 25, "text": "SE", "continent": "Task"}, {"value": 26, "text": "SP", "continent": "Task"}, {"value": 27, "text": "TO", "continent": "Task"}]';
  
  function autocomplete(inp, arr, tp) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/

    var currentFocus;
    var z = 0;

    /* console.log('teste');
    if (tp == 'estado') {
      if (estados_execute.length > 0) {
        const index = connectors.indexOf(estados_execute[estados_execute.length - 1]);
        if (index == -1) {
          arr = connectors;
        }
        else {
          arr.push(...not);
        }
      }
      else {
        arr.push(...not);
      }
    } */

    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          //if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
            z ++;
            b = document.createElement("DIV");
            b.setAttribute("class", "tag-items");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong'>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function(e) {
                /*insert the value for the autocomplete text field:*/
                inp.value = this.getElementsByTagName("input")[0].value;
                /*close the list of autocompleted values,
                (or any other open lists of autocompleted values:*/
                closeAllLists();
            });
            if (z <= 10)
              a.appendChild(b);
          }
        }
        z = 0;
    });

    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        //console.log(e);
        if (e.keyCode == 40) {
          /*If the arrow DOWN key is pressed,
          increase the currentFocus variable:*/
          currentFocus++;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /*If the arrow UP key is pressed,
          decrease the currentFocus variable:*/
          currentFocus--;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 13) {
          
          /*If the ENTER key is pressed, prevent the form from being submitted,*/
          e.preventDefault();
          if (currentFocus <= -1)
            currentFocus = 0;
          if (currentFocus > -1) {
            /*and simulate a click on the "active" item:*/
            if (x) 
            {
              if (x[currentFocus].click())
                x[currentFocus].click()
              if (inp.getAttribute('name') == "txt_estados")
                $('#add_estado').click()
              else if (inp.getAttribute('name') == "txt_mercados")
                $('#add_mercado').click()
              else if (inp.getAttribute('name') == "txt_stacks")
                $('#add_stack').click()
              //create_button(inp.getAttribute('name'));
            }
          }
        }
    });
    function addActive(x) {
      
     
      /*a function to classify an item as "active":*/
      if (!x) return false;
      /*start by removing the "active" class on all items:*/
      removeActive(x);
      
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /*add class "autocomplete-active":*/
      x[currentFocus].style.backgroundColor = "aliceblue";
      x[currentFocus].style.color = "blueviolet"
      //x[currentFocus].classList.add("autocomplete-active");
      //console.log(x[currentFocus]);
    }
    function removeActive(x) {
      /*a function to remove the "active" class from all autocomplete items:*/
      for (var i = 0; i < x.length; i++) {
        x[i].style.color = "black"
        x[i].style.backgroundColor = "bisque";
      }
    }
    function closeAllLists(elmnt) {
      /*close all autocomplete lists in the document,
      except the one passed as an argument:*/
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      /*var x = e.target.getElementById(this.id);
            
      if (x) 
            {
              x[currentFocus].click();
              if (e.getAttribute('name') == "txt_estados")
                $('#add_estado').click()
              else if (e.getAttribute('name') == "txt_mercados")
                $('#add_mercado').click()
              else if (e.getAttribute('name') == "txt_stacks")
                $('#add_stack').click()
              //create_button(inp.getAttribute('name'));
            }*/
      /* console.log("e",e);
      console.log("target",e.target.parentElement.getElementById(this.id)); */

      closeAllLists(e.target);
  });
  }
  