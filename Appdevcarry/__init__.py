from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateMemberForm, CreateGuestForm
import shelve, Member, Guest
from Member import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/cart')
def cart():
    db = shelve.open('cart.db', 'c')
    try:
        cart_dict = db['Cart']

    except:
        cart = cart.cart()



        return render_template('cart.html')


@app.route('/createMember', methods=['GET', 'POST'])
def create_member():
    create_member_form = CreateMemberForm(request.form)
    if request.method == 'POST' and create_member_form.validate():
        members_dict = {}
        db = shelve.open('member.db', 'c')
        try:
            members_dict = db['Members']
        except:
            print("Error in retrieving Members from member.db.")
        member = Member.Member(create_member_form.first_name.data, create_member_form.last_name.data,
                               create_member_form.gender.data, create_member_form.email.data,
                               create_member_form.address.data, create_member_form.birthday.data,
                               create_member_form.payment_method.data, create_member_form.credit_number.data,
                               create_member_form.exp_number.data, create_member_form.remarks.data)
        members_dict[member.get_member_id()] = member
        db['Members'] = members_dict
        db.close()
        return redirect(url_for('retrieve_members'))
    return render_template('createMember.html', form=create_member_form)


@app.route('/createGuest', methods=['GET', 'POST'])
def create_guest():
    create_guest_form = CreateGuestForm(request.form)
    if request.method == 'POST' and create_guest_form.validate():
        guests_dict = {}
        db = shelve.open('guest.db', 'c')
        try:
            guests_dict = db['Guests']
        except:
            print("Error in retrieving Guests from guest.db.")
        guest = Guest.Guest(create_guest_form.address.data, create_guest_form.payment_method.data,
                            create_guest_form.credit_number.data, create_guest_form.exp_number.data,
                            create_guest_form.remarks.data)
        guests_dict[guest.get_guest_id()] = guest
        db['Guests'] = guests_dict
        db.close()
        return redirect(url_for('retrieve_guests'))
    return render_template('createGuest.html', form=create_guest_form)


@app.route('/retrieveMembers')
def retrieve_members():
    members_dict = {}
    db = shelve.open('member.db', 'r')
    members_dict = db['Members']
    db.close()
    members_list = []
    for key in members_dict:
        member = members_dict.get(key)
        members_list.append(member)
    return render_template('retrieveMembers.html', count=len(members_list), members_list=members_list)

@app.route('/loginMember')
def login_members():

    db = shelve.open('member.db', 'r')
    db.close()





@app.route('/retrieveGuests')
def retrieve_guests():
    guests_dict = {}
    db = shelve.open('guest.db', 'r')
    guests_dict = db['Guests']
    db.close()
    guests_list = []
    for key in guests_dict:
        guest = guests_dict.get(key)
        guests_list.append(guest)
    return render_template('retrieveGuests.html', count=len(guests_list), guests_list=guests_list)


@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    orders_dict = {}
    db = shelve.open('order.db', 'w')
    orders_dict = db['Orders']
    orders_dict.pop(id)
    db['Orders'] = orders_dict
    db.close()
    return redirect(url_for('cart'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # firstname = request.form['firstname']
    # lastname = request.form['lastname']
    # gender = request.form['gender']
    # email = request.form['email']
    # birthday = request.form['birthday']
    update_member_form = CreateMemberForm(request.form)

    members_dict = {}
    db = shelve.open('member.db', 'r')
    if db['Members'] != {}:
        members_dict = db['Members']
    else:
        db['Members'] = members_dict
    member1 = Member(update_member_form.first_name.data, update_member_form.last_name.data, update_member_form.gender.data, update_member_form.email.data, update_member_form.birthday.data, update_member_form.address, update_member_form.payment_method, update_member_form.credit_number, update_member_form.exp_number, update_member_form.remarks.data)
    member1.set_payment_method(update_member_form.payment_method)
    member1.set_credit_number(update_member_form.credit_number)
    member1.set_exp_number(update_member_form.exp_number)
    member1.set_remarks(update_member_form.remarks.data)
    members_dict[member1.__class__.count_id] = member1
    db['Members'] = members_dict
    db.close()

@app.route('/updateMember/<int:id>/', methods=['GET', 'POST'])
def update_member(id):
    update_member_form = CreateMemberForm(request.form)
    if request.method == 'POST' and update_member_form.validate():
        members_dict = {}
        db = shelve.open('member.db', 'w')
        members_dict = db['Members']

        member = members_dict.get(id)
        member.set_first_name(update_member_form.first_name.data)
        member.set_last_name(update_member_form.last_name.data)
        member.set_gender(update_member_form.gender.data)
        member.set_email(update_member_form.email.data)
        member.set_birthday(update_member_form.birthday)
        member.set_address(update_member_form.address)
        member.set_payment_method(update_member_form.payment_method)
        member.set_credit_number(update_member_form.credit_number)
        member.set_exp_number(update_member_form.exp_number)
        member.set_remarks(update_member_form.remarks.data)

        db['Members'] = members_dict
        db.close()

        return redirect(url_for('retrieve_members'))

    else:
        members_dict = {}
        db = shelve.open('member.db', 'r')
        members_dict = db['Members']
        db.close()

        member = members_dict.get(id)

        update_member_form.first_name.data = member.get_first_name()
        update_member_form.last_name.data = member.get_last_name()
        update_member_form.gender.data = member.get_gender()
        update_member_form.email.data = member.get_email()
        update_member_form.birthday.data = member.get_birthday()
        update_member_form.address.data = member.get_address()
        update_member_form.payment_method.data = member.get_payment_metod()
        update_member_form.credit_number.data = member.get_credit_number()
        update_member_form.exp_number.data = member.get_exp_number()
        update_member_form.remarks.data = member.get_remarks()
        return render_template('UpdateMember.html', form=update_member_form)

@app.route('/deleteMember/<int:id>', methods=['POST'])
def delete_member(id):
    member_dict = {}
    db = shelve.open('member.db', 'w')
    members_dict = db['Members']
    members_dict.pop(id)
    db['Members'] = members_dict

    db.close()

    return redirect(url_for('retrieve_members'))

if __name__ == '__main__':
    app.run()
