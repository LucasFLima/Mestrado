package br.jus.tse.eleitoral.eleitor.dominio.negocio.models;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlType;

import br.jus.tse.corporativa.arqjeespring.negocio.models.AbstractPersistentModel;

@Entity
@Table(name="OCUPACAO")
@XmlType(name = "Ocupacao")
@XmlAccessorType(XmlAccessType.FIELD)
public class Ocupacao extends AbstractPersistentModel<String> {

	private static final long serialVersionUID = 1L;
	
	@Id
	@Column(name="COD_OBJETO")
	private String id;

	@Column(name="SITUACAO")
	private Integer codigoSitaucao;

	@Column(name="NUM_OCUPACAO")
	private Integer numeroOcupacao;

	@Column(name="DES_OCUPACAO")
	private String descricaoOcupacao;

	@Column(name="NOM_OCUPACAO_CS")
	private String nomeOcupacaoCS;

	@Column(name="GRAU_INSTRUCAO_MIN")
	private String codigoGrauInstrucaoMinimo;


	public Ocupacao() {
	}


	public String getId() {
		return id;
	}


	public void setId(String id) {
		this.id = id;
	}


	public Integer getCodigoSitaucao() {
		return codigoSitaucao;
	}


	public void setCodigoSitaucao(Integer codigoSitaucao) {
		this.codigoSitaucao = codigoSitaucao;
	}


	public Integer getNumeroOcupacao() {
		return numeroOcupacao;
	}


	public void setNumeroOcupacao(Integer numeroOcupacao) {
		this.numeroOcupacao = numeroOcupacao;
	}


	public String getDescricaoOcupacao() {
		return descricaoOcupacao;
	}


	public void setDescricaoOcupacao(String descricaoOcupacao) {
		this.descricaoOcupacao = descricaoOcupacao;
	}


	public String getNomeOcupacaoCS() {
		return nomeOcupacaoCS;
	}


	public void setNomeOcupacaoCS(String nomeOcupacaoCS) {
		this.nomeOcupacaoCS = nomeOcupacaoCS;
	}


	public String getCodigoGrauInstrucaoMinimo() {
		return codigoGrauInstrucaoMinimo;
	}


	public void setCodigoGrauInstrucaoMinimo(String codigoGrauInstrucaoMinimo) {
		this.codigoGrauInstrucaoMinimo = codigoGrauInstrucaoMinimo;
	}


}