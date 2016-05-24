package br.jus.tse.eleitoral.eleitor.integracao.webservices.dto;

import java.util.List;


public class LocalVotacaoDTO {
	private String inscricao;
	private String nomEleitor;
	private Integer numZona;
	private Integer numSecao;
	private String codObjetoLocal;
	private String nomLocal;
	private String desEndereco;
	private String nomBairro;
	private String nomMunicipio;
	private String sglUf;
	private LocalVotacaoAgregacaoDTO localVotacaoAgregacao;
	private LocalVotacaoTemporarioDTO localVotacaoTemporario;
	private List<LocalVotacaoTransitoDTO> localVotacaoTransito;
	
	public String getNomLocal() {
		return nomLocal;
	}
	public String getInscricao() {
		return inscricao;
	}
	public void setInscricao(String inscricao) {
		this.inscricao = inscricao;
	}
	public String getNomEleitor() {
		return nomEleitor;
	}
	public void setNomEleitor(String nomEleitor) {
		this.nomEleitor = nomEleitor;
	}
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
	public String getNomMunicipio() {
		return nomMunicipio;
	}
	public void setNomMunicipio(String nomMunicipio) {
		this.nomMunicipio = nomMunicipio;
	}
	public String getSglUf() {
		return sglUf;
	}
	public void setSglUf(String sglUf) {
		this.sglUf = sglUf;
	}

	public LocalVotacaoAgregacaoDTO getLocalVotacaoAgregacao() {
		return localVotacaoAgregacao;
	}
	public void setLocalVotacaoAgregacao(LocalVotacaoAgregacaoDTO localVotacaoAgregacao) {
		this.localVotacaoAgregacao = localVotacaoAgregacao;
	}
	public LocalVotacaoTemporarioDTO getLocalVotacaoTemporario() {
		return localVotacaoTemporario;
	}
	public void setLocalVotacaoTemporario(LocalVotacaoTemporarioDTO localVotacaoTemporario) {
		this.localVotacaoTemporario = localVotacaoTemporario;
	}
	public List<LocalVotacaoTransitoDTO> getLocalVotacaoTransito() {
		return localVotacaoTransito;
	}
	public void setLocalVotacaoTransito(List<LocalVotacaoTransitoDTO> localVotacaoTransito) {
		this.localVotacaoTransito = localVotacaoTransito;
	}

}
