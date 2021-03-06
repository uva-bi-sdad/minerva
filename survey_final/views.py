from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from numpy.random import binomial

class SocioDemographic(Page):
    form_model = models.Player
    is_debug = False

    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']

    def makeCheckTable(self, qName, choices, table_rows):
                      
        header = ''.join(['<th class="verticalTableHeader"><div><p>{}</p></div></th>'.format(c) for c in choices])
        row = """
            <tr>
                <td><div class="row-text">{}</div></td>
                {}
            </tr>
            """
            
        def make_data_row(field,i):
            cells = []
            for c in choices:
                i += 1
                title = 'q14_{}_{}X{}'.format(i,field[0],c)
                field_name = "id_{}".format(title)
                name = field
                data_row = """
                    <td><div class="btnRadio">
                        <label class="checkbox no-margin" for="{}">
                            <input type="checkbox" id="{}" value=True name="{}"> 
                        </label>
                    </div></td>
                """.format(field_name, field_name, title)
                cells.append(data_row)
            
            return ''.join(cells), i           
        
        rows = []
        i = 0
        for table_row in table_rows:
            data, i = make_data_row(table_row, i)             
            rows.append(row.format(table_row[1],data))
                
        rows = '\n'.join(rows)
            
            
        out_str = """<table class="table table-condensed fixed" summary="" >
          <colgroup>
    <col style="background-color:white; width: 400px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
  </colgroup>
    <thead>
        <tr>
            <th></th>
            {}
        </tr>    
    </thead>
    <tbody>
        {}
    </tbody>
    </table>"""
        return out_str.format(header,rows)

    def makeTable(self, qName = 'q12'):
        fields = [fname for fname in self.form_model._meta.get_all_field_names() if fname.startswith(qName)]
        fields = sorted(fields)
        rows = []
        choices = self.form_model._meta.get_field_by_name(fields[0])[0].choices
                      
        header = ''.join(['<th class="verticalTableHeader"><div><p>{}</p></div></th>'.format(c[0]) for c in choices])

        def make_data_row(field):
            cells = []
            i = 0
            for c in choices:
                field_name = "id_{}_{}".format(field,i+1)
                name = field
                i += 1
                data_row = """
                <td><div class="btnRadio">
                <label class="radio-inline" for="{}">
                <input type="radio" id="{}" value="{}" name="{}" required> 
                </label>
                </div></td>""".format(field_name, field_name, c[0], name)
                cells.append(data_row)
            
            return ''.join(cells)           
        row = """
        <tr>
            <td><div class="row-text">{}</div></td>
            {}
        </tr>
        """ 
        for field in fields:
            F = self.form_model._meta.get_field_by_name(field)
            f = F[0]
            
            if f.choices:
                rows.append(row.format(f.verbose_name,make_data_row(field)))
                
        rows = '\n'.join(rows)
            
            
        out_str = """<table class="table table-condensed fixed" summary="" >
          <colgroup>
    <col style="background-color:white; width: 400px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
  </colgroup>
    <thead>
        <tr>
            <th></th>
            {}
        </tr>    
    </thead>
    <tbody>
        {}
    </tbody>
    </table>"""
        return out_str.format(header,rows)   
    
    

    def vars_for_template(self):

        columns = [
            'Facebook',
            'Twitter',
            'LinkedIn',
            'Instagram',
            'Reddit',
            'WhatsApp',
            'Meetup',
            'Nextdoor',
            'Snapchat',
            'Weibo',
            'WeChat',        
        ]
        
        rows = [
            ("prof_network", "Professional networking"),
            ("soc_network", "Social networking"),
            ("xchng_info", "Exchange of information with peers and family"),
            ("soc_events","Organize and/or attend social events"),
            ("pol_events","Organize and/or attend political events"),
            ("news_info", "News and Information about people and places"),
            ("job", "Job seeking"),
            ("money", "To make money"),
            ("games", "To play games"),
            ("research", "Research"),
#            ("other", "Other"),
            ("used_sites","Select the sites that you use a couple of times a week"),
        ]        
        
        return {
            'q13Table':  self.makeTable('q13').replace('\n',''),
            'q14Table':  self.makeCheckTable('q14', columns, rows),
            'q15Table':  self.makeTable('q15').replace('\n',''),       
        }


class SocioDemographic13(SocioDemographic):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
        
    def get_form_fields(self):
        questions = [
#            "q13a_transportation",
            "q13b_volunteer",
            "q13c_donations",
            "q13d_discussPolitics",
            "q13e_communicate",
            "q13f_demonstrate",
            "q13g_elections",
            "q13h_risk",
        ]  
        
        return questions
    
class SocioDemographic14(SocioDemographic):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
    def get_form_fields(self):
        questions = [
            "q14_l_networking_otherPrint",             
        ]

        columns = [
            'Facebook',
            'Twitter',
            'LinkedIn',
            'Instagram',
            'Reddit',
            'WhatsApp',
            'Meetup',
            'Nextdoor',
            'Snapchat',
            'Weibo',
            'WeChat',        
        ]
        
        rows = [
            ("prof_network", "Professional networking"),
            ("soc_network", "Social networking"),
            ("xchng_info", "Exchange of information with peers and family"),
            ("soc_events","Organize and/or attend social events"),
            ("pol_events","Organize and/or attend political events"),
            ("news_info", "News and Information about people and places"),
            ("job", "Job seeking"),
            ("money", "To make money"),
            ("games", "To play games"),
            ("research", "Research"),
#            ("other", "Other"),
            ("used_sites","Select the sites that you use a couple of times a week"),
        ]
        i = 0
        for r in rows:
            for c in columns:
                i += 1
                field_name = 'q14_{}_{}X{}'.format(i, r[0], c)
                questions += [field_name]        
        
        return questions


class SocioDemographic15(SocioDemographic):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
    def get_form_fields(self):
        questions = [
            "q15a_ethics_wealth",
            "q15b_ethics_climate",
            "q15c_ethics_gunControl",
#            "q15d_ethics_admissions",
#            "q15e_ethics_taxes",      
        ]
        return questions


class Behavioral2(Page):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
            
    form_model = models.Player
    form_fields = [
        "trust_1",
        "trust_2",
        "trust_3",
        "trust_4",
    ]
    
    template_name = "survey_final/Behavioral2.html"


class Behavioral1(Page):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
    form_model = models.Player
    form_fields = [
        "daringness",
    ] + ['coinScenerio_{}'.format(i) for i in range(1, 32)]
    
    def vars_for_template(self):
        return {'coinOffers': [{"num": i, "amt": 10 * (i - 1)} for i in range(1, 32)]}
        

class Paid(Page):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
    form_model = models.Player
    form_fields = [
        "risky_project",
        "risky_project_2",
    ]
        
    def before_next_page(self):
        self.player.payoff = 0

        xRate = .016667        
        
        amtInvested = self.player.risky_project
        game_outcome = binomial(1,.4)
        self.player.risky_project_outcome = game_outcome
        self.player.payoff += (200. * xRate * amtInvested * .01 * 3.) * game_outcome + (200. - 200. * amtInvested * .01) * xRate       
        
        amtInvested = self.player.risky_project_2
        game_outcome = binomial(1,.5)
        self.player.risky_project_outcome_2 = game_outcome
        self.player.payoff += (200. * xRate * amtInvested * .01 * 2.5) * game_outcome + (200. - 200. * amtInvested * .01) * xRate  


class Results(Page):
    def is_displayed(self):
        if self.session.is_demo:
            return True
        else:
            return self.participant.vars['consent']
    def vars_for_template(self):
        return {
            'payoff_currency': self.participant.payoff.to_real_world_currency(self.session) - self.player.payoff.to_real_world_currency(self.session),
            'payoff_risk_assessment': self.player.payoff.to_real_world_currency(self.session),
        }


page_sequence = [
    SocioDemographic13,
    SocioDemographic14,
    SocioDemographic15,
    Behavioral2,
    Behavioral1,
    Paid,
    Results
]
