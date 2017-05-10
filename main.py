import os

import MySQLdb
import webapp2

from flask import Flask, render_template, request
# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')


def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(



def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD
            )

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
#    else:
#        db = MySQLdb.connect(
#            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD)

    return db
db = connect_to_cloudsql()
cursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    #cursor.execute("""select * from test.user limit 1;""")
#    return('%s' %(cursor.fetchall()[0][-2]))
    return render_template('index2.html')

app = Flask(__name__)

@app.route('/')
def index():
    #cursor.execute("""select * from test.user limit 1;""")
#    return('%s' %(cursor.fetchall()[0][-2]))
    return render_template('index2.html')

@app.route('/input_name')
def show_input_name():
    return render_template('input_name.html')


@app.route('/user_detail', methods=['POST'])
def third():

    # Input user number
    num = request.form['inputnumber']
def show_input_name():
    return render_template('input_name.html')


@app.route('/user_detail', methods=['POST'])
def third():

    # Input user number
    num = request.form['inputnumber']
    number = int(num)

    # Summary user information
    cursor.execute("""select * from test.user LIMIT %s,1;""" %number)
    self = cursor.fetchall()[0]
    self_user_id = self[0]
    self_user_city = self[1]
    self_user_name = self[3]
    # Summary user information
    cursor.execute("""select * from test.user LIMIT %s,1;""" %number)
    self = cursor.fetchall()[0]
    self_user_id = self[0]
    self_user_city = self[1]
    self_user_name = self[3]


    # Random Walk to predict restaurant
    cursor.execute("""select * from test.business_recommend LIMIT %s,1;""" %num$
    business_recommend = cursor.fetchall()[0]
    business1 = business_recommend[2]
    business2 = business_recommend[3]
    business3 = business_recommend[4]
    categories1 = business_recommend[5]
    categories2 = business_recommend[6]
    categories3 = business_recommend[7]
   # Collaborative filtering to predict meal partner
    cursor.execute("""select * from test.user_recommend LIMIT %s,1;""" %number)
    user_recommend = cursor.fetchall()[0]
    user_recommend_number1 = user_recommend[2]
    user_recommend_number2 = user_recommend[3]
    user_recommend_number3 = user_recommend[4]

    # Meal partner 1
    cursor.execute("""select * from test.user LIMIT %s,1;""" %(int(user_recomme$
    user_recommend_1 = cursor.fetchall()[0]
    user_recommend_1_name = user_recommend_1[3]
    user_recommend_1_fan = user_recommend_1[2]
    user_recommend_1_review = user_recommend_1[4]
    user_recommend_1_useful = user_recommend_1[5]

#    return('%s' %user_recommend_1_name)
    # Meal partner 2
    cursor.execute("""select * from test.user LIMIT %s,1;""" %(int(user_recomme$
    user_recommend_2 = cursor.fetchall()[0]
    user_recommend_2_name = user_recommend_2[3]
    user_recommend_2_fan = user_recommend_2[2]
    user_recommend_2_review = user_recommend_2[4]
    user_recommend_2_useful = user_recommend_2[5]

    # Meal partner 3
    cursor.execute("""select * from test.user LIMIT %s,1;""" %(int(user_recomme$
    user_recommend_3 = cursor.fetchall()[0]
    user_recommend_3_name = user_recommend_3[3]
    user_recommend_3_fan = user_recommend_3[2]
    user_recommend_3_review = user_recommend_3[4]
    user_recommend_3_useful = user_recommend_3[5]

#    return('%s' %user_recommend_3_name)
#    return('%s' %(user_recommend_1_name))
    return render_template('user_detail.html',
                           self_name=self_user_name,
                           number=[user_recommend_number1, user_recommend_numbe$
                           name=[user_recommend_1_name, user_recommend_2_name, $
                           city=self_user_city,
                           business_name=[business1, business2, business3],
                           fans=[user_recommend_1_fan, user_recommend_2_fan, us$
                           useful=[user_recommend_1_useful, user_recommend_2_us$
                           rcount=[user_recommend_1_review, user_recommend_2_re$
                           )

if __name__ == "__main__":
    app.run(debug=True)









