package br.jus.tse.eleitoral.eleitor.dominio.negocio.enums;

public enum SituacaoInscricaoEnum {
	REGULAR(0, "Regular"), 
	CANCELADO(4, "Cancelada"), 
	SUSPENSO(6, "Suspensa"), 
	NAO_LIBERADO(7, "Não Liberada"), 
	LIBERADO(9, "Liberada");

	private final int codigo;
	private final String descricao;

	private SituacaoInscricaoEnum(int _codigo, String _descricao) {
		this.codigo = _codigo;
		this.descricao = _descricao;
	}

	public int getCodigo() {
		return this.codigo;
	}

	public String getDescricao() {
		return this.descricao;
	}

	public static SituacaoInscricaoEnum valueOf(int _codigo)
			throws IllegalArgumentException {
		SituacaoInscricaoEnum value = null;
		for (SituacaoInscricaoEnum element : values()) {
			if (element.getCodigo() == _codigo) {
				value = element;
				break;
			}
		}
		if (value == null) {
			throw new IllegalArgumentException(String.valueOf(_codigo));
		}
		return value;
	}
}
