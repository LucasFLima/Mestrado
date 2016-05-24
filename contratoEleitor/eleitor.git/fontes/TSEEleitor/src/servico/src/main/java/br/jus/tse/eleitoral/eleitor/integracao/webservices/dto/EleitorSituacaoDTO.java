package br.jus.tse.eleitoral.eleitor.integracao.webservices.dto;

import br.jus.tse.eleitoral.eleitor.dominio.negocio.enums.SituacaoInscricaoEnum;

public class EleitorSituacaoDTO {
	private String inscricao;
	private String nome;
	private SituacaoInscricaoEnum situacao;
	
	public String getInscricao() {
		return inscricao;
	}
	public void setInscricao(String inscricao) {
		this.inscricao = inscricao;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public SituacaoInscricaoEnum getSituacao() {
		return situacao;
	}
	public void setSituacao(SituacaoInscricaoEnum situacao) {
		this.situacao = situacao;
	}
	
}
