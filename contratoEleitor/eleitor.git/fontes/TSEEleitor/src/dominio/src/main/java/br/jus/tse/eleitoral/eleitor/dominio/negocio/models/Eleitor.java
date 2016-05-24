package br.jus.tse.eleitoral.eleitor.dominio.negocio.models;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlType;

import br.jus.tse.corporativa.arqjeespring.negocio.models.AbstractPersistentModel;
import br.jus.tse.eleitoral.estruturaje.dominio.negocio.models.SecaoEleitoral;

@Entity 
@Table(name="ELEITOR")
@XmlType(name = "Eleitor")
@XmlAccessorType(XmlAccessType.FIELD)
public class Eleitor extends AbstractPersistentModel<String> {
	private static final long serialVersionUID = 1L;

	@Id
	@Column(name="COD_OBJETO")
	private String id;

	@Column(name="COD_ESTADO_CIVIL")
	private Integer codEstadoCivil;

	@Column(name="COD_FON_MAE")
	private String codFonMae;

	@Column(name="COD_FON_NOME_ELEITOR")
	private String codFonNomeEleitor;

	@Column(name="COD_FON_PAI")
	private String codFonPai;

	@Column(name="COD_GRAU_INSTR")
	private Integer codGrauInstr;

	@Column(name="COD_OBJETO_BAIRRO")
	private String codObjetoBairro;

	@Column(name="COD_OBJETO_LOGRADOURO")
	private String codObjetoLogradouro;

	@Column(name="COD_OBJETO_MUNIC_NASC")
	private String codObjetoMunicNasc;

	@Column(name="COD_OBJETO_MUNICIPIO_COLETA")
	private String codObjetoMunicipioColeta;

	@Column(name="COD_OBJETO_OCUPACAO")
	private String codObjetoOcupacao;

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "COD_OBJETO_SECAO")
	private SecaoEleitoral secao;

	@Column(name="COD_SEXO")
	private Integer codSexo;

	@Column(name="COD_SIT_ELEITOR")
	private Integer codSitEleitor;

	@Temporal(TemporalType.DATE)
	@Column(name="DAT_DOMIC_MUNIC")
	private Date datDomicMunic;

	@Temporal(TemporalType.DATE)
	@Column(name="DAT_DOMIC_UF")
	private Date datDomicUf;

	@Column(name="DAT_NASC")
	private Integer datNasc;

	@Column(name="DES_COMPLEMENTO")
	private String desComplemento;

	@Column(name="DES_ENDERECO")
	private String desEndereco;

	@Column(name="NOM_ELEITOR")
	private String nomEleitor;

	@Column(name="NOM_ELEITOR_LIMPO")
	private String nomEleitorLimpo;

	@Column(name="NOM_MAE")
	private String nomMae;

	@Column(name="NOM_MAE_LIMPO")
	private String nomMaeLimpo;

	@Column(name="NOM_PAI")
	private String nomPai;

	@Column(name="NOM_PAI_LIMPO")
	private String nomPaiLimpo;

	@Column(name="NUM_CEP")
	private String numCep;

	@Column(name="NUM_CPF")
	private String numCpf;

	@Column(name="NUM_DOCUMENTO")
	private String numDocumento;

	@Column(name="NUM_ENDERECO")
	private Integer numEndereco;

	@Column(name="NUM_INSCRICAO")
	private String numInscricao;

	@Column(name="NUM_REGISTRO_CIVIL")
	private Integer numRegistroCivil;

	@Column(name="NUM_TEL_ELEITOR")
	private String numTelEleitor;

	@Column(name="NUM_TEL_ELEITOR_2")
	private String numTelEleitor2;

	@Column(name="ORG_EXPEDIDOR")
	private String orgExpedidor;

	@Column(name="TIP_DOCUMENTO")
	private Integer tipDocumento;

	public Eleitor() {
	}

	public String getId() {
		return id;
	}
	
	public void setId(String id) {
		this.id = id;
	}

	public Integer getCodEstadoCivil() {
		return this.codEstadoCivil;
	}

	public void setCodEstadoCivil(Integer codEstadoCivil) {
		this.codEstadoCivil = codEstadoCivil;
	}

	public String getCodFonMae() {
		return this.codFonMae;
	}

	public void setCodFonMae(String codFonMae) {
		this.codFonMae = codFonMae;
	}

	public String getCodFonNomeEleitor() {
		return this.codFonNomeEleitor;
	}

	public void setCodFonNomeEleitor(String codFonNomeEleitor) {
		this.codFonNomeEleitor = codFonNomeEleitor;
	}

	public String getCodFonPai() {
		return this.codFonPai;
	}

	public void setCodFonPai(String codFonPai) {
		this.codFonPai = codFonPai;
	}

	public Integer getCodGrauInstr() {
		return this.codGrauInstr;
	}

	public void setCodGrauInstr(Integer codGrauInstr) {
		this.codGrauInstr = codGrauInstr;
	}

	public String getCodObjetoBairro() {
		return this.codObjetoBairro;
	}

	public void setCodObjetoBairro(String codObjetoBairro) {
		this.codObjetoBairro = codObjetoBairro;
	}

	public String getCodObjetoLogradouro() {
		return this.codObjetoLogradouro;
	}

	public void setCodObjetoLogradouro(String codObjetoLogradouro) {
		this.codObjetoLogradouro = codObjetoLogradouro;
	}

	public String getCodObjetoMunicNasc() {
		return this.codObjetoMunicNasc;
	}

	public void setCodObjetoMunicNasc(String codObjetoMunicNasc) {
		this.codObjetoMunicNasc = codObjetoMunicNasc;
	}

	public String getCodObjetoMunicipioColeta() {
		return this.codObjetoMunicipioColeta;
	}

	public void setCodObjetoMunicipioColeta(String codObjetoMunicipioColeta) {
		this.codObjetoMunicipioColeta = codObjetoMunicipioColeta;
	}

	public String getCodObjetoOcupacao() {
		return this.codObjetoOcupacao;
	}

	public void setCodObjetoOcupacao(String codObjetoOcupacao) {
		this.codObjetoOcupacao = codObjetoOcupacao;
	}

/*
	public String getCodObjetoSecao() {
		return this.codObjetoSecao;
	}

	public void setCodObjetoSecao(String codObjetoSecao) {
		this.codObjetoSecao = codObjetoSecao;
	}
*/
	
	public SecaoEleitoral getSecao() {
		return this.secao;
	}

	public void setSecao(SecaoEleitoral secao) {
		this.secao = secao;
	}

	public Integer getCodSexo() {
		return this.codSexo;
	}

	public void setCodSexo(Integer codSexo) {
		this.codSexo = codSexo;
	}

	public Integer getCodSitEleitor() {
		return this.codSitEleitor;
	}

	public void setCodSitEleitor(Integer codSitEleitor) {
		this.codSitEleitor = codSitEleitor;
	}

	public Date getDatDomicMunic() {
		return this.datDomicMunic;
	}

	public void setDatDomicMunic(Date datDomicMunic) {
		this.datDomicMunic = datDomicMunic;
	}

	public Date getDatDomicUf() {
		return this.datDomicUf;
	}

	public void setDatDomicUf(Date datDomicUf) {
		this.datDomicUf = datDomicUf;
	}

	public Integer getDatNasc() {
		return this.datNasc;
	}

	public void setDatNasc(Integer datNasc) {
		this.datNasc = datNasc;
	}

	public String getDesComplemento() {
		return this.desComplemento;
	}

	public void setDesComplemento(String desComplemento) {
		this.desComplemento = desComplemento;
	}

	public String getDesEndereco() {
		return this.desEndereco;
	}

	public void setDesEndereco(String desEndereco) {
		this.desEndereco = desEndereco;
	}

	public String getNomEleitor() {
		return this.nomEleitor;
	}

	public void setNomEleitor(String nomEleitor) {
		this.nomEleitor = nomEleitor;
	}

	public String getNomEleitorLimpo() {
		return this.nomEleitorLimpo;
	}

	public void setNomEleitorLimpo(String nomEleitorLimpo) {
		this.nomEleitorLimpo = nomEleitorLimpo;
	}

	public String getNomMae() {
		return this.nomMae;
	}

	public void setNomMae(String nomMae) {
		this.nomMae = nomMae;
	}

	public String getNomMaeLimpo() {
		return this.nomMaeLimpo;
	}

	public void setNomMaeLimpo(String nomMaeLimpo) {
		this.nomMaeLimpo = nomMaeLimpo;
	}

	public String getNomPai() {
		return this.nomPai;
	}

	public void setNomPai(String nomPai) {
		this.nomPai = nomPai;
	}

	public String getNomPaiLimpo() {
		return this.nomPaiLimpo;
	}

	public void setNomPaiLimpo(String nomPaiLimpo) {
		this.nomPaiLimpo = nomPaiLimpo;
	}

	public String getNumCep() {
		return this.numCep;
	}

	public void setNumCep(String numCep) {
		this.numCep = numCep;
	}

	public String getNumCpf() {
		return this.numCpf;
	}

	public void setNumCpf(String numCpf) {
		this.numCpf = numCpf;
	}

	public String getNumDocumento() {
		return this.numDocumento;
	}

	public void setNumDocumento(String numDocumento) {
		this.numDocumento = numDocumento;
	}

	public Integer getNumEndereco() {
		return this.numEndereco;
	}

	public void setNumEndereco(Integer numEndereco) {
		this.numEndereco = numEndereco;
	}

	public String getNumInscricao() {
		return this.numInscricao;
	}

	public void setNumInscricao(String numInscricao) {
		this.numInscricao = numInscricao;
	}

	public Integer getNumRegistroCivil() {
		return this.numRegistroCivil;
	}

	public void setNumRegistroCivil(Integer numRegistroCivil) {
		this.numRegistroCivil = numRegistroCivil;
	}

	public String getNumTelEleitor() {
		return this.numTelEleitor;
	}

	public void setNumTelEleitor(String numTelEleitor) {
		this.numTelEleitor = numTelEleitor;
	}

	public String getNumTelEleitor2() {
		return this.numTelEleitor2;
	}

	public void setNumTelEleitor2(String numTelEleitor2) {
		this.numTelEleitor2 = numTelEleitor2;
	}

	public String getOrgExpedidor() {
		return this.orgExpedidor;
	}

	public void setOrgExpedidor(String orgExpedidor) {
		this.orgExpedidor = orgExpedidor;
	}

	public Integer getTipDocumento() {
		return this.tipDocumento;
	}

	public void setTipDocumento(Integer tipDocumento) {
		this.tipDocumento = tipDocumento;
	}

}