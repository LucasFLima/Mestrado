package br.jus.tse.eleitoral.eleitor.dominio.tests;

import junit.framework.Assert;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import br.jus.tse.eleitoral.eleitor.dominio.negocio.managers.IEleitorManager;

public class EleitorTest extends Assert {

	@Autowired
	private IEleitorManager iEleitorManager;
	
	@Test
	public void testBuscarEleitorPeloNumeroInscricao() {
		
		// teste aqui
		
		assertEquals(true, true);
	}
	
}
