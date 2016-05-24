package br.jus.tse.eleitoral.eleitor.dominio.negocio.exceptions;

public class EleitorNaoInformadoException extends Exception {

	private static final long serialVersionUID = 1L;

	public EleitorNaoInformadoException() {
        super();
    }

    public EleitorNaoInformadoException(String message) {
        super(message);
    }

    public EleitorNaoInformadoException(String message, Throwable cause) {
        super(message, cause);
    }
	
}
