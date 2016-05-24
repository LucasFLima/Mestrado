package br.jus.tse.eleitoral.eleitor.dominio.negocio.models;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import br.jus.tse.corporativa.arqjeespring.negocio.models.AbstractPersistentModel;

@Entity
@Table(name="VW_LOCAL_VOTACAO_TEMPORARIO")
public class ViewLocalVotacaoTemporario extends AbstractPersistentModel<String> {
	private static final long serialVersionUID = 1L;

	@Id
	@Column(name="COD_OBJETO")
	private String codObjetoEleitor;

	@Column(name="NUM_INSCRICAO")
	private String numInscricao;

	@Column(name="DAT_NASC")
	private Integer datNasc;

	@Column(name="NOM_ELEITOR")
	private String nomEleitor;

	@Column(name="NOM_ELEITOR_LIMPO")
	private String nomEleitorLimpo;

	@Column(name="NOM_MAE")
	private String nomMae;

	@Column(name="NOM_MAE_LIMPO")
	private String nomMaeLimpo;

	@Column(name="COD_FON_NOME_ELEITOR")
	private String codFonNomeEleitor;

	@Column(name="COD_FON_MAE")
	private String codFonMae;

	@Column(name="COD_OBJETO_DAT_ELEICAO")
	private String codObjetoDataEleicao;

	@Column(name="COD_OBJETO_LOCAL")
	private String codObjetoLocal;

	@Column(name="UF")
	private String sglUf;

	@Column(name="NOM_LOCAL")
	private String NomLocal;

	@Column(name="DES_ENDERECO")
	private String DesEndereco;

	@Column(name="NOM_BAIRRO")
	private String NomBairro;

	@Column(name="NOM_LOCALIDADE")
	private String NomLocalidade;

	@Column(name="NUM_ZONA")
	private Integer NumZona;

	@Column(name="NUM_SECAO")
	private Integer NumSecao;

	public String getCodObjetoEleitor() {
		return codObjetoEleitor;
	}

	public void setCodObjetoEleitor(String codObjetoEleitor) {
		this.codObjetoEleitor = codObjetoEleitor;
	}

	public String getNumInscricao() {
		return numInscricao;
	}

	public void setNumInscricao(String numInscricao) {
		this.numInscricao = numInscricao;
	}

	public Integer getDatNasc() {
		return datNasc;
	}

	public void setDatNasc(Integer datNasc) {
		this.datNasc = datNasc;
	}

	public String getNomEleitor() {
		return nomEleitor;
	}

	public void setNomEleitor(String nomEleitor) {
		this.nomEleitor = nomEleitor;
	}

	public String getNomEleitorLimpo() {
		return nomEleitorLimpo;
	}

	public void setNomEleitorLimpo(String nomEleitorLimpo) {
		this.nomEleitorLimpo = nomEleitorLimpo;
	}

	public String getNomMae() {
		return nomMae;
	}

	public void setNomMae(String nomMae) {
		this.nomMae = nomMae;
	}

	public String getNomMaeLimpo() {
		return nomMaeLimpo;
	}

	public void setNomMaeLimpo(String nomMaeLimpo) {
		this.nomMaeLimpo = nomMaeLimpo;
	}

	public String getCodFonNomeEleitor() {
		return codFonNomeEleitor;
	}

	public void setCodFonNomeEleitor(String codFonNomeEleitor) {
		this.codFonNomeEleitor = codFonNomeEleitor;
	}

	public String getCodFonMae() {
		return codFonMae;
	}

	public void setCodFonMae(String codFonMae) {
		this.codFonMae = codFonMae;
	}

	public String getCodObjetoDataEleicao() {
		return codObjetoDataEleicao;
	}

	public void setCodObjetoDataEleicao(String codObjetoDataEleicao) {
		this.codObjetoDataEleicao = codObjetoDataEleicao;
	}

	public String getCodObjetoLocal() {
		return codObjetoLocal;
	}

	public void setCodObjetoLocal(String codObjetoLocal) {
		this.codObjetoLocal = codObjetoLocal;
	}

	public String getSglUf() {
		return sglUf;
	}

	public void setSglUf(String sglUf) {
		this.sglUf = sglUf;
	}

	public String getNomLocal() {
		return NomLocal;
	}

	public void setNomLocal(String nomLocal) {
		NomLocal = nomLocal;
	}

	public String getDesEndereco() {
		return DesEndereco;
	}

	public void setDesEndereco(String desEndereco) {
		DesEndereco = desEndereco;
	}

	public String getNomBairro() {
		return NomBairro;
	}

	public void setNomBairro(String nomBairro) {
		NomBairro = nomBairro;
	}

	public String getNomLocalidade() {
		return NomLocalidade;
	}

	public void setNomLocalidade(String nomLocalidade) {
		NomLocalidade = nomLocalidade;
	}

	public Integer getNumZona() {
		return NumZona;
	}

	public void setNumZona(Integer numZona) {
		NumZona = numZona;
	}

	public Integer getNumSecao() {
		return NumSecao;
	}

	public void setNumSecao(Integer numSecao) {
		NumSecao = numSecao;
	}

	@Override
	public String getId() {
		return codObjetoEleitor;
	}

	@Override
	public void setId(String codObjetoEleitor) {
		this.codObjetoEleitor = codObjetoEleitor;
	}


}
