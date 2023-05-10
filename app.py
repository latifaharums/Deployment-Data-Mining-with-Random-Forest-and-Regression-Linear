import streamlit as st
from PIL import Image
import assets
import pickle

favIcon = Image.open('./assets/img/favicon.ico')

st.set_page_config(
	page_title="Kelompok 5 Data Mining",
	page_icon=favIcon,
	layout="wide",
	initial_sidebar_state="expanded",
)

# untuk menyembunyikan footer
hideFooter = '''
<style>
.css-cio0dv {display: none;}
'''
st.markdown(hideFooter, unsafe_allow_html=True)

# untuk menyembunyikan menu sebelah kanan
hideRightMenu = '''
<style>
#mainMenu {display: none;}
'''
st.markdown(hideRightMenu, unsafe_allow_html=True)

def load_model(dir):
	model = pickle.load(open(dir, "rb"))
	return model
def detail_kelompok():
	st.columns(3)[1].header('Detail Kelompok 5')

	st.subheader('Sumber Dataset : ')
	st.markdown('<a href="https://www.kaggle.com/datasets/meirnizri/covid19-dataset" target="_blank">https://www.kaggle.com/datasets/meirnizri/covid19-dataset</a>', unsafe_allow_html=True)
	
	st.subheader('Nama Anggota Kelompok :')
	st.markdown(
	'''
	  1. Denis Fitri Salsabila (202103002)\n
	  2. Latifah Arum Sulistianingsih (202103008)\n
	  3. Mohamad Burhanudin (202103034)
	''')

def predict():
	model = load_model("./assets/models/modelCovid19RandomForest.pkl")
	st.columns(3)[1].header("Prediksi")
	col1, col2 = st.columns(2)

	#PATIENT_TYPE
	options = {"Rumah": 1, "Rumah Sakit": 2}
	selected_value = col1.selectbox("Dimana anda melakukan isolasi?", options.keys())
	PATIENT_TYPE = options[selected_value]

	#AGE
	AGE = col2.slider(
		'Berapa usia anda?',
		0, 100
	)

	# USMR
	options = {"Ya": 1, "Tidak": 2}
	selected_value = col1.selectbox("Apakah anda dirawat rumah sakit?", options.keys())
	USMR = options[selected_value]

	#Unit Medis
	MEDICAL_UNIT = col2.selectbox(
		'Unit Medis',
    (1,2,3,4,5,6,7,8,9,10,11,12,13)
	)

	#PNEUMONIA
	options = {"Ya": 1, "Tidak": 2}
	selected_value = col1.selectbox("Apakah anda mempunyai penyakit Pneumonia?", options.keys())
	PNEUMONIA = options[selected_value]

	#PREGNANT
	selected_value = col2.selectbox("Apakah anda sedang hamil?", options.keys())
	PREGNANT = options[selected_value]

	#DIABETES
	selected_value = col1.selectbox("Apakah anda mempunyai penyakit diabetes?", options.keys())
	DIABETES = options[selected_value]

	#COPD
	selected_value = col2.selectbox("Apakah anda mempunyai penyakit paru kronis?", options.keys())
	COPD = options[selected_value]

	#INMSUPR
	selected_value = col1.selectbox("Apakah anda mempunyai penyakit Imunosupresi?", options.keys())
	INMSUPR = options[selected_value]

	#HIPERTENTION
	selected_value = col2.selectbox("Apakah anda mempunyai penyakit Hipertensi?", options.keys())
	HIPERTENTION = options[selected_value]

	#OTHER_DISEASE
	selected_value = col1.selectbox("Apakah anda mempunyai riwayat Penyakit Lainnya?", options.keys())
	OTHER_DISEASE = options[selected_value]

	#CARDIOVASCULAR
	selected_value = col2.selectbox("Apakah anda mempunyai penyakit terkait jantung atau pembuluh darah?", options.keys())
	CARDIOVASCULAR = options[selected_value]

	#OBESITY
	selected_value = col1.selectbox("Apakah anda mengalami obesitas?", options.keys())
	OBESITY = options[selected_value]

	#RENAL_CHRONIC
	selected_value = col2.selectbox("Apakah anda mempunyai penyakit Ginjal Kronis?", options.keys())
	RENAL_CHRONIC = options[selected_value]

	#TOBACCO
	selected_value = col1.selectbox("Apakah anda perokok?", options.keys())
	TOBACCO = options[selected_value]

	#CLASIFFICATION_FINAL
	selected_value = col2.selectbox("Apa hasil tes covid anda?", options.keys())
	CLASIFFICATION_FINAL = options[selected_value]

	def predict():
		hasil_prediksi = model.predict([[USMR, MEDICAL_UNIT, PATIENT_TYPE, PNEUMONIA, AGE, PREGNANT, DIABETES, COPD, INMSUPR, HIPERTENTION, OTHER_DISEASE, CARDIOVASCULAR, OBESITY, RENAL_CHRONIC, TOBACCO, CLASIFFICATION_FINAL]])
		# hasil_prediksi = model.predict([[2, 1, 1, 2, 64, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]]) #hidup
		# hasil_prediksi = model.predict([[2, 1, 1, 1, 65,2, 2, 2, 2, 1,2,2,2,2,2,1]]) #mati
		if hasil_prediksi == 1:
			return st.columns(3)[1].error('Anda diprediksi Meninggal')
		elif hasil_prediksi == 2:
			return st.columns(3)[1].success('Anda diprediksi Hidup')
			
	if st.columns(5)[2].button('predict'):
		predict()
	else:
		st.write('')


def main():
	st.sidebar.image(Image.open('assets/img/unjaya.png'),width=250)
	selection = st.sidebar.selectbox("", ["Detail-Kelompok", "Predict"])

	if selection == "Detail-Kelompok":
		detail_kelompok()
	elif selection == "Predict":
		predict()

if __name__ == '__main__':
	main()