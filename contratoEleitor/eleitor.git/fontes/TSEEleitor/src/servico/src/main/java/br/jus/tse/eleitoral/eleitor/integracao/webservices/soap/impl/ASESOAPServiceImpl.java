package br.jus.tse.eleitoral.eleitor.integracao.webservices.soap.impl;

import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

import org.springframework.beans.factory.annotation.Autowired;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.WebServicesException;
import br.jus.tse.corporativa.arqjeespring.infra.utils.conversores.ConversorTipoObjeto;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.managers.IEleitorManager;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.ASEDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.soap.IASESOAPService;

@WebService(
	endpointInterface = "br.jus.tse.eleitoral.eleitor.integracao.webservices.soap.IASESOAPService",
	targetNamespace = "http://tse.jus.br/eleitoral/eleitor",
	portName = "ASEPort"
)
@SOAPBinding(style = Style.RPC)
public class ASESOAPServiceImpl implements IASESOAPService {

	@Autowired
	private IEleitorManager iEleitorManager;
	
	@Autowired
	private ConversorTipoObjeto conversorTipoObjeto;

	@Override
	public String inserirASE(ASEDTO aseDTO) throws WebServicesException {
		// TODO Auto-generated method stub
		return null;
	}

}
