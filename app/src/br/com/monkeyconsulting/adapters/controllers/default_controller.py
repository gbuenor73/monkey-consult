from flask import render_template
from flask.views import MethodView


class Defaultcontroller(MethodView):

    def get(self, pagina):
        if pagina == 'header':
            return render_template('headers/header.html')

        elif pagina == 'footer':
            return render_template('footers/footer.html')
