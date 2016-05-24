package br.jus.tse.eleitoral.eleitor.dominio.negocio.exceptions;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.RegraNegocioException;

public class ParametroObrigatorioNaoInformadoException extends RegraNegocioException {

	private static final long serialVersionUID = 1L;

	public ParametroObrigatorioNaoInformadoException() {
        super("Parâmetro obrigatório na pesquisa não foi informado.");
    }

    public ParametroObrigatorioNaoInformadoException(String message) {
        super(message);
    }

    public ParametroObrigatorioNaoInformadoException(String message, Throwable cause) {
        super(message, cause);
    }
	
}
