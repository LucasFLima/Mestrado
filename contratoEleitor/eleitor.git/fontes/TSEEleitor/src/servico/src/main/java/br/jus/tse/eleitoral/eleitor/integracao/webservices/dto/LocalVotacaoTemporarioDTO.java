package br.jus.tse.eleitoral.eleitor.integracao.webservices.dto;

public class LocalVotacaoTemporarioDTO {
	private Integer numZona;
	private Integer numSecao;
	private String codObjetoLocal;
	private String nomLocal;
	private String desEndereco;
	private String nomBairro;
	private String nomLocalidade;
	private String sglUf;
	
	public Integer getNumZona() {
		return numZona;
	}
	public void setNumZona(Integer numZona) {
		this.numZona = numZona;
	}
	public Integer getNumSecao() {
		return numSecao;
	}
	public void setNumSecao(Integer numSecao) {
		this.numSecao = numSecao;
	}
	public String getCodObjetoLocal() {
		return codObjetoLocal;
	}
	public void setCodObjetoLocal(String codObjetoLocal) {
		this.codObjetoLocal = codObjetoLocal;
	}
	public String getNomLocal() {
		return nomLocal;
	}
	public void setNomLocal(String nomLocal) {
		this.nomLocal = nomLocal;
	}
	public String getDesEndereco() {
		return desEndereco;
	}
	public void setDesEndereco(String desEndereco) {
		this.desEndereco = desEndereco;
	}
	public String getNomBairro() {
		return nomBairro;
	}
	public void setNomBairro(String nomBairro) {
		this.nomBairro = nomBairro;
	}
	public String getNomLocalidade() {
		return nomLocalidade;
	}
	public void setNomLocalidade(String nomLocalidade) {
		this.nomLocalidade = nomLocalidade;
	}
	public String getSglUf() {
		return sglUf;
	}
	public void setSglUf(String sglUf) {
		this.sglUf = sglUf;
	}
}
