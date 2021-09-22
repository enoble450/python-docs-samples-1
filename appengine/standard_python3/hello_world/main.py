# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'All rise for the jury. Please be seated.\nMembers of the jury, I understand you have a verdict.\nMembers of the Jury, I will now read the verdicts as they will appear in the permanent records of the Fourth Judicial District, State of Minnesota, County of Hennepin, District Court, Fourth Judicial District.\nState of Minnesota, Plaintiff versus Derek Michael Chauvin, Defendant.\n\nVerdict, Count One.\nCourt file number 27 CR 2012646.\nWe, the Jury, in the above entitled matter as to count one, Unintentional Second Degree Murder While Committing a Felony, find the defendant GUILTY.\nThis verdict agreed to this 20th day of April, 2021, at 1:44 PM. Signed Juror Foreperson, Juror Number 19.'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
