package br.jus.tse.eleitoral.eleitor.dominio.negocio.exceptions;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.RegraNegocioException;

public class InscricaoInexistenteException extends RegraNegocioException {

	private static final long serialVersionUID = 1L;

	public InscricaoInexistenteException() {
        super("Número de Inscrição inexistente");
    }

    public InscricaoInexistenteException(String message) {
        super(message);
    }

    public InscricaoInexistenteException(String message, Throwable cause) {
        super(message, cause);
    }
	
}
