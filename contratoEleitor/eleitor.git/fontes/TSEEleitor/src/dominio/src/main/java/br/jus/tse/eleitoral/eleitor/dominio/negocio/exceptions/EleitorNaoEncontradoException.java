package br.jus.tse.eleitoral.eleitor.dominio.negocio.exceptions;

public class EleitorNaoEncontradoException extends Exception {

	private static final long serialVersionUID = 1L;

	public EleitorNaoEncontradoException() {
        super();
    }

    public EleitorNaoEncontradoException(String message) {
        super(message);
    }

    public EleitorNaoEncontradoException(String message, Throwable cause) {
        super(message, cause);
    }
	
}
