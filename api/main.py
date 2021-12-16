from fastapi import FastAPI, Request
# from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from Log import Log
import pandas as pd

load_dotenv(dotenv_path='../login.env')
log = Log()
db = pd.read_sql_query("SELECT * FROM empresa_completa3 WHERE 1", log.con)

app = FastAPI()
templates = Jinja2Templates(directory="frontend/html")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.route("/")
def choose(request: Request):
    return templates.TemplateResponse('index.html',    
                                  context={'request': request})
@app.route("/mercados_list")
def get_mercados(request: Request):
    mercados_ori = ['Advertising', 'S/N', 'Vendas e Marketing', 'Recursos Humanos', 'Meio Ambiente', 'Indústria', 'Internet', 'Transportes', 'Energia', 'Seguros', 'Infantil', 'Direito', 'Automobilismo', 'Educação', 'E-commerce', 'Gestão', 'Saúde e Bem-estar', 'Produtos de Consumo', 'Cloud Computing', 'Outros', 'Mobile', 'Games', 'TIC e Telecom', 'Logística e Mobilidade Urbana', 'Desenvolvimento de Software', 'Hardware', 'Imobiliário', 'Biotecnologia', 'Finanças', 'Varejo / Atacado', 'Esportes', 'Comunicação e Mídia', 'Agronegócio', 'Serviços Profissionais', 'CRM', 'Nanotecnologia', 'Big Data', 'Pets', 'Construção Civil', 'Segurança e Defesa', 'Casa e Família', 'Entretenimento', 'Eventos e Turismo', 'Moda e Beleza', 'Recrutamento', 'Video']
    
    return templates.TemplateResponse('list.html',
                                      context={'request': request, "lists": mercados_ori, "name":"Mercados"})

@app.route("/estados_list")
def get_mercados(request: Request):
    estados_ori = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'TODOS'];
    
    return templates.TemplateResponse('list.html',
                                      context={'request': request, "lists": estados_ori,"name":"Estados"})

@app.route("/stacks_list")
def get_mercados(request: Request):
    stacks_ori = ['.NET', '.NET 4.5', '.NET Core', '.NET MVC', '4D', 'ABAP', 'Ably Realtime', 'ABNF', 'ACDSee', 'Ada', 'Administrador de sistema', 'Adobe Air', 'Adobe Flash', 'Adobe Flash Builder', 'Adobe Flex', 'Adobe PhoneGap', 'AdonisJS', 'ADVPL', 'ADVPL ASP', 'Agavi', 'Agda', 'AgilePHP', 'AGS Script', 'Ajax', 'AlertOps', 'Algolia', 'Alloy', 'Amazon API Gateway', 'Amazon AppStream', 'Amazon Aurora', 'Amazon DynamoDB', 'Amazon ElastiCache', 'Amazon Elasticsearch Service', 'Amazon RDS for MariaDB', 'Amazon RDS for MySQL', 'Amazon Rekognition', 'Amazon Relational Database Service (RDS)', 'Amazon Simple Notification Service (SNS)', 'Amazon Simple Workflow Service (SWF)', 'Amazon SimpleDB', 'amCharts', 'AMP', 'Android', 'Android Studio', 'Angular', 'Angularjs', 'ANTLR', 'Apache', 'Apache ActiveMQ', 'Apache Cassandra', 'Apache Cocoon', 'Apache Commons', 'Apache Cordova', 'Apache Drill', 'Apache Giraph', 'Apache Groovy', 'Apache HAWQ', 'Apache Impala', 'Apache jclouds', 'Apache Jena', 'Apache Kafka', 'Apache NetBeans', 'Apache Nutch', 'Apache Phoenix', 'Apache POI', 'Apache Qpid', 'Apache Sling', 'Apache Solr', 'Apache Struts', 'Apache Tika', 'Apache Tiles', 'Apache Wicket', 'Apex', 'API', 'Appbot', 'Apple Safari', 'AppleScript', 'ArcGIS', 'ArcGIS Online', 'ArcGIS Pro', 'Arduino', 'ARKit', 'ASN.1', 'ASP', 'ASP.NET', 'ASP.NET Core', 'ASP.NET MVC', 'Assembly', 'Atom', 'Aura', 'AWS Amplify', 'AWS Chatbot', 'AWS Cloud9', 'AWS EC2 (Elastic Compute Cloud)', 'AWS Mobile Services', 'AWS RDS (Relational Database Service)', 'AWS S3', 'AWS Step Functions', 'AWS Transit Gateway', 'AWS Trusted Advisor', 'Azure', 'Azure API Management', 'Azure Arc', 'Azure Cognitive Services', 'Azure Computer Vision', 'Azure HDInsight', 'Azure Redis Cache', 'Azure Stack', 'Azure Stack HCI', 'Azure Web Apps', 'Back4App', 'Backbone.js', 'Backendless', 'Bandwidth', 'Bash', 'Beamer', 'Big Data', 'Bing Maps', 'BizTalk Server', 'BizTalk Server 2009', 'BizTalk Server 2010', 'BizTalk Server 2013', 'BizTalk Server 2013 R2', 'BizTalk Server 2016', 'Blade', 'Blockchain', 'Bootstrap', 'Browser Update', 'Bulma', 'C', 'C#', 'C++', 'CA IDMS', 'CA InterTest', 'CakePHP', 'Celery Project', 'CGI::Application', 'Chartbeat', 'Chrome', 'Clean', 'Clean Code', 'Clojure', 'Cloud', 'CloudAMQP', 'CMake', 'COBOL', 'CocoaPods', 'Cocos2d-X', 'CodeIgniter', 'CoffeeScript', 'Cognitect', 'ColdFusion', 'ColdFusion CFC', 'Common Lisp', 'Component Pascal', 'Composer', 'Continuous Delivery', 'Continuous Integration', 'Cordova', 'Couchbase', 'CouchDB', 'CreateJS', 'Crystal', 'CSS', 'CSV', 'Cucumber', 'Cuda', 'Cycript', 'Cypress.io', 'D', 'D2C.io', 'Dart', 'Dassault Systemes', 'Data science', 'DataStax', 'DataTables', 'Datawrapper', 'DB2', 'Dell Boomi', 'Delphi', 'Design Pattern', 'desktop', 'DevOps', 'DIGITAL Command Language', 'Discord', 'Django', 'DM', 'DNS Zone', 'Docker', 'Dockerfile', 'Doctrine', 'Dogescript', 'Dojo', 'Domino 8', 'Drupal', 'Duet Enterprise', 'DynamoDB', 'Dynatrace', 'eC', 'ECLiPSe', 'Eclipse AspectJ', 'Eclipse Jetty', 'ECMAScript', 'egghead.io', 'EJB', 'EJS', 'Elastic Cloud', 'Elasticsearch', 'Elfsight', 'Elixir', 'Ember.js', 'EmberJS', 'Entity framework', 'ERP', 'ES6', 'Estimote', 'Excel', 'Express', 'eXtreme Programming', 'F#', 'Facebook SDK', 'Feathers', 'Fiddler', 'Figma', 'FileMaker', 'FileZilla', 'Firebase', 'Firebird', 'Firebug', 'Flask', 'Flex', 'FlexSlider', 'Flickr API', 'Flot', 'Flutter', 'FLUX', 'Font Awesome', 'Forth', 'Foundation', 'FreeMarker', 'Froala Editor', 'FuelPHP', 'Funnel', 'Game Maker Language', 'GameMaker', 'GDScript', 'Git', 'GLSL', 'Glyphicons', 'Go', 'Google Analytics', 'Google Charts', 'Google Cloud', 'Google Cloud Apigee', 'Google Cloud APIs', 'Google Cloud Bigtable', 'Google Cloud Datastore', 'Google Cloud Endpoints', 'Google Cloud Firestore', 'Google Cloud Messaging', 'Google Cloud SDK', 'Google Cloud Search', 'Google Cloud Spanner', 'Google Cloud Vision API', 'Google Custom Search', 'Google Dialogflow', 'Google Gaming', 'Google Go Language', 'Google Maps Platform', 'Google Search Appliance', 'Google Web Designer', 'Google Web Toolkit', 'GoPlay (Formerly Smartpixel)', 'Gradle', 'Grails', 'Grammatical Framework', 'GraphQL', 'Gravatar', 'Groovy', 'Gulp', 'Gulpjs', 'GWT', 'Halcyon', 'Hanami', 'Handlebars', 'Hazelcast', 'Heroku', 'Hibernate', 'Highcharts', 'HLSL', 'Horde', 'Hornetq', 'Hortonworks', 'HTML', 'HTTP', 'Hugo', 'HybridJava', 'Hybris', 'HydraMVC', 'IAR Embedded Workbench', 'IBM API Connect', 'IBM Cloud Paks', 'IBM Cloud Private', 'IBM HTTP Server', 'IBM ILOG', 'IBM Informix', 'IBM Lotus', 'IBM MobileFirst', 'IBM MQ', 'IBM Rational ClearQuest', 'IBM Rational Rose', 'IBM Sterling Control Center', 'IBM Sterling File Gateway', 'IBM VTAM', 'IBM Watson Discovery', 'IBM Watson Explorer', 'InfluxData', 'Infogram', 'IntelliJ IDEA', 'ionCube PHP Encoder', 'Ionic', 'iOS', 'Ireport', 'Jade', 'Jasmin', 'Jasper', 'Java', 'Java Server Pages', 'JavaEE', 'JavaScript', 'JavaScriptMVC', 'JBoss', 'JBoss Enterprise Web Server (EWS)', 'JCL', 'Jekyll', 'Jenkins', 'Jest', 'JFlex', 'Jitpack', 'jqPlot', 'jQuery', 'JQuery UI', 'JS Bin', 'JSF', 'JSON', 'JSX', 'JUnit', 'Jupyter Notebook', 'K2', 'Kanban', 'Kite', 'Knockout', 'Koa', 'Kohana', 'Kore.ai', 'Kotlin', 'kubernetes', 'Kubernetes-native', 'LabVIEW', 'Laravel', 'Layer7', 'Layer7 API Management', 'Lean', 'Less', 'LibGDX', 'LightBox', 'LightWidget', 'Linux', 'Linux Kernel Module', 'Liquibase', 'Liquid', 'list.js', 'Lodash', 'Logos', 'Lua', 'LUMEN', 'Machine learning', 'Magento', 'MariaDB', 'Material Design Lite', 'Materialize', 'Materialize CSS', 'Mathematica', 'MathJax', 'Matlab', 'Maven POM', 'MemSQL', 'Meteor', 'Micronaut', 'Microsoft Azure', 'Microsoft Azure App Service', 'Microsoft Azure Automation Account', 'Microsoft Azure Bot Service', 'Microsoft Azure Front Door', 'Microsoft Azure Maps', 'Microsoft Azure Spring Cloud', 'Microsoft Bing', 'Microsoft DirectX', 'Microsoft FAST ESP', 'Microsoft Hyper-V Server', 'Microsoft Intune', 'Microsoft Team Foundation Server', 'Microsoft TypeScript', 'Microsoft Virtual Server', 'Microsoft Visual Basic', 'Microsoft Visual FoxPro', 'Microsoft Visual Studio', 'Microsoft.NET', 'Modernizr', 'Module Management System', 'Moment Timezone', 'Moment.js', 'MongoDB', 'Monkey', 'Mootools', 'Mozilla Firefox', 'MQL5', 'MVC', 'MVVM', 'MySQL', 'Nazar', 'NetLinx', 'NextJS', 'Nginx', 'Node.js', 'NodeJS', 'NonStop SQL', 'NoSQL', 'Notepad++', 'NPM', 'NSQ', 'NumPy', 'Objective-C', 'Objective-C++', 'Objective-J', 'OBS', 'Odoo', 'Omgrofl', 'OnBarcode', 'OnGraph', 'OnPage', 'Opa', 'Open JDK HotSpot', 'OpenCL', 'OpenCV', 'Openlayers', 'OpenSSL', 'ORACLE', 'Oracle 11i', 'Oracle ADF Faces', 'Oracle API Gateway', 'Oracle API Manager', 'Oracle API Platform', 'Oracle Database', 'Oracle Fusion Middleware', 'OWl Carousel', 'Pandas', 'Parse', 'Pascal', 'Perl', 'Phabricator', 'Phalcon', 'Phaser', 'Phoenix', 'PhoneGap', 'Photoshop', 'PHP', 'PhpStorm', 'PHPUnit', 'pip python', 'Pivotal tc Server', 'Play', 'PLSQL', 'Pod', 'Polyfill', 'Polymer', 'POO', 'PostgreSQL', 'Postman', 'PostScript', 'PowerBuilder', 'PowerShell', 'POWr', 'pre-commit', 'Prebid', 'Prebid.js', 'Processing', 'Progress', 'Protocol Buffer', 'Prototype', 'Puppet', 'Pure', 'Pure CSS', 'PureMVC', 'PWA', 'PyCharm', 'Pyramid', 'PyTest', 'Python', 'PyTorch', 'QA - Quality Assurance', 'Qlikview', 'QML', 'Qualys Web Application Scanning', 'Quarkus', 'Quartz Scheduler', 'Quasar', 'R', 'RabbitMQ', 'Ragel in Ruby Host', 'RAML', 'RawGit', 'React', 'React Native', 'ReactiveX', 'ReactJS', 'REALbasic', 'Realtime Framework', 'Redis', 'Redux', 'RenderScript', 'RequireJS', 'RESTful', 'RestfulX', 'Retool', 'Riot.js', 'RobotFramework', 'RPM Spec', 'RStudio', 'Ruby', 'Ruby on Rails', 'Rust', 'S.O.L.I.D', 'Sails.js', 'Salesforce', 'Salesforce Lightning Web Components', 'Salesforce Maps', 'SAP', 'SAP HANA', 'SAS', 'SAS Base', 'Sass', 'Scala', 'Scandit', 'Scikit-learn', 'SCORM', 'Script.Aculo.us', 'SCRUM', 'SCSS', 'Select2', 'Selenium', 'Semantic.ui', 'SEO', 'Server', 'Serverless', 'Service Virtualization', 'Sharepoint', 'Shell', 'Shell Script', 'Sinatra', 'Slim', 'Smarty', 'Snap', 'SnapWidget', 'Socket.io', 'Solace', 'Spring', 'Spring Boot', 'Spring Cloud', 'Spring Framework', 'Spring MVC', 'SQF', 'SQL', 'SQL Server', 'SQLite', 'SQLPL', 'StarUML', 'Stencyl', 'Stripes', 'Struts', 'Styled-Components', 'Sublime Text', 'SuperCollider', 'SVG', 'Swift', 'Swiftlet', 'Symfony', 'Syncro', 'T-SQL', 'Tachyons', 'TDD', 'TensorFlow', 'Terra', 'Testes automatizados', 'Testes de Regressão', 'Testes Funcionais', 'Testes unitários', 'The Jupyter Notebook', 'three.js', 'Thymeleaf', 'TI Program', 'TIBCO ActiveSpaces', 'TIBCO FTL', 'TIBCO Managed File Transfer', 'TIBCO Mashery', 'TickCounter', 'TinyMCE', 'Tomcat', 'Tornado', 'TweenMax', 'Twig', 'Typekit', 'TypeScript', 'UIkit', 'UML', 'Underscore.js', 'Unity', 'Unity3D Asset', 'Unix', 'Unreal Engine', 'UnrealScript', 'Vaadin', 'Valve', 'Vanilla', 'VB .NET', 'VB.NET', 'VBA', 'VCL', 'Vercel', 'Vert.x', 'Vertx', 'VictorOps', 'Video.js', 'Vim', 'vis.js', 'Visual Basic', 'Visual Basic.NET', 'Visual Studio Code', 'VMware Tanzu GemFire', 'VTEX', 'Vue.js', 'Web API', 'Web Services', 'web2py', 'webMethods API Gateway', 'Webtask', 'Weeby.co', 'WooCommerce', 'WordPress', 'WPF', 'Xamarin', 'XC', 'Xcode', 'XML', 'XQuery', 'XSLT', 'Yii', 'Zend', 'Zepto', 'Zepto.js', 'Zope'];
    
    return templates.TemplateResponse('list.html',
                                      context={'request': request, "lists": stacks_ori, "name":"Stacks"})


@app.get("/dropdown")
def dropdown():
    #return ", ".join(['Advertising', 'S/N', 'Vendas e Marketing', 'Recursos Humanos', 'Meio Ambiente', 'Indústria', 'Internet', 'Transportes', 'Energia', 'Seguros', 'Infantil', 'Direito', 'Automobilismo', 'Educação', 'E-commerce', 'Gestão', 'Saúde e Bem-estar', 'Produtos de Consumo', 'Cloud Computing', 'Outros', 'Mobile', 'Games', 'TIC e Telecom', 'Logística e Mobilidade Urbana', 'Desenvolvimento de Software', 'Hardware', 'Imobiliário', 'Biotecnologia', 'Finanças', 'Varejo / Atacado', 'Esportes', 'Comunicação e Mídia', 'Agronegócio', 'Serviços Profissionais', 'CRM', 'Nanotecnologia', 'Big Data', 'Pets', 'Construção Civil', 'Segurança e Defesa', 'Casa e Família', 'Entretenimento', 'Eventos e Turismo', 'Moda e Beleza', 'Recrutamento', 'Video'])
    return 'ola<br>ola3/nteste\nteste2</br>oi'
@app.get("/search")
def get_info(market: str, stack: str, state: str, file_name: str='untitled', get_csv : bool = False):
    stack = stack.replace("Cpp","C\+\+")
    stack = stack.replace("Csharp","C#")
    print(stack)

    query = ""
    if not file_name:
        file_name = 'Untitled'
    file_name += '.csv'

    if state and state != 'TODOS':
        state_query = "(estado==' " + state.replace(',', "' or estado==' ") + "')"
        query += state_query
        if market:
            query += ' and '
            market_query = "(mercado=='" + market.replace(',', "' or mercado=='") + "')"
            query += market_query
        if stack:
            query += ' and '
            stacks = stack.split(',')
            for i in range(len(stacks)):
                query += f'stacks.str.contains("{stacks[i]}", na=False).values'
                if i < len(stacks) - 1:
                    query += ' or '
    elif market:
        market_query = "(mercado=='" + market.replace(',', "' or mercado=='") + "')"
        query += market_query
        if stack:
            query += ' and '
            stacks = stack.split(',')
            for i in range(len(stacks)):
                query += f'stacks.str.contains("{stacks[i]}", na=False).values'
                if i < len(stacks) - 1:
                    query += ' or '
    elif stack:
        stacks = stack.split(',')
        for i in range(len(stacks)):
            query += f'stacks.str.contains("{stacks[i]}", na=False).values'
            if i < len(stacks) - 1:
                query += ' or '
    else:
        return 0
    print(query)
    df = db.query(query)
    if get_csv:
        df.to_csv(file_name, sep=',', index=False)
        return FileResponse(file_name, filename=file_name)
    else:
        return len(df.index)
